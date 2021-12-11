from PySide6.QtCore import QFile, QIODevice, QDataStream
from PySide6.QtGui import QImageReader, QImage

from os import walk, mkdir, path
from PIL import Image, ImageQt


# Converts GIF into images.
def convert_gif_into_frames(filepath):
    image = Image.open(filepath)
    # palette = image.getpalette()

    frames = []
    try:
        while True:
            # image.putpalette(palette)
            frame = Image.new('RGBA', image.size)
            frame.paste(image)

            frames.append(ImageQt.ImageQt(frame))

            image.seek(image.tell() + 1)
    except EOFError:
        pass

    return frames


# Locate saves:
def check_for_saves():
    if path.isdir('./saves/'):
        for _, _, files in walk('./saves/'):
            for file in files:
                if file.endswith('.buddy'):
                    return file


# Buddy file:
class BuddyFile:
    def __init__(self, name='', profile_path='', buddy_path=''):
        # Profile Picture:
        image_reader = QImageReader(profile_path)
        if image_reader.supportsAnimation() and image_reader.imageCount() > 1:
            self.profile_picture = convert_gif_into_frames(profile_path)
        else:
            self.profile_picture = [QImage(profile_path)]

        # Mini Buddy Picture:
        image_reader = QImageReader(buddy_path)
        if image_reader.supportsAnimation() and image_reader.imageCount() > 1:
            self.buddy_picture = convert_gif_into_frames(buddy_path)
        else:
            self.buddy_picture = [QImage(buddy_path)]

        self.name = name


def save_buddy(buddy_file: BuddyFile, filename):
    mkdir(f'./saves/{filename}')

    # Serializing:
    file = QFile(f"./saves/{filename}/{filename}.buddy")
    file.open(QIODevice.WriteOnly)

    # Stream & Magic Number & Version:
    out = QDataStream(file)
    out.writeInt32(0x0000C0D1)

    # Name:
    out.writeString(buddy_file.name)

    # Profile Picture(s):
    profile_frame_size = len(buddy_file.profile_picture)
    if profile_frame_size == 1:
        out.writeInt8(0x0A)
        if isinstance(buddy_file.profile_picture[0], QImage):
            out << buddy_file.profile_picture[0]
        else:
            raise Exception('When saving single image, received an invalid profile picture type.')
    else:
        out.writeInt8(0x0B)
        if isinstance(buddy_file.profile_picture, list):
            out.writeInt16(profile_frame_size)
            for frame in buddy_file.profile_picture:
                out << frame
        else:
            raise Exception('When saving multiple images, received an invalid profile picture type.')

    # Buddy Picture(s):
    mini_buddy_frame_size = len(buddy_file.buddy_picture)
    if mini_buddy_frame_size == 1:
        out.writeInt8(0x0A)
        if isinstance(buddy_file.buddy_picture[0], QImage):
            out << buddy_file.buddy_picture[0]
        else:
            print(type(buddy_file.buddy_picture))
            raise Exception('When saving single image, received an invalid profile picture type.')
    else:
        out.writeInt8(0x0B)
        if isinstance(buddy_file.buddy_picture, list):
            out.writeInt16(mini_buddy_frame_size)
            for frame in buddy_file.buddy_picture:
                out << frame
        else:
            raise Exception('When saving multiple images, received an invalid profile picture type.')

    file.close()


# Load:
def load_buddy(filepath, filename):
    print(filename)
    if not filename:
        filename = check_for_saves()
        if not filename:
            return

    filename = filename.replace('.buddy', '')

    # Deserializing:
    file = QFile(f"./saves/{filename}/{filename}.buddy")
    file.open(QIODevice.ReadOnly)

    # Stream & Magic Number & Version:
    out = QDataStream(file)
    magic = out.readInt32()

    if not magic == 0x0000C0D1:
        raise Exception('Version or validation number mismatch.')

    # Name:
    name = out.readString()

    # Profile Picture:
    profile_type = out.readInt8()
    if profile_type == 0x0A:
        profile_image = QImage()
        out >> profile_image
    elif profile_type == 0x0B:
        frame_count = out.readInt16()
        profile_image = []
        for _ in range(frame_count):
            image = QImage()
            out >> image

            profile_image.append(image)
    else:
        raise Exception('Profile type not found.')

    # Profile Picture:
    buddy_type = out.readInt8()
    if buddy_type == 0x0A:
        buddy_image = QImage()
        out >> buddy_image
    elif buddy_type == 0x0B:
        frame_count = out.readInt16()
        buddy_image = []
        for _ in range(frame_count):
            image = QImage()
            out >> image

            buddy_image.append(image)
    else:
        raise Exception('Buddy type not found.')

    return {'name': name, 'profile_picture': profile_image, 'mini_buddy_picture': buddy_image}
