from PySide6.QtCore import QFile, QIODevice, QDataStream
from PySide6.QtGui import QImageReader, QImage
from os import walk, mkdir, path, listdir
from PIL import Image, ImageQt


# Converts GIF into images.
def convert_gif_into_frames(filepath):
    image = Image.open(filepath)

    frames = []
    try:
        while True:
            frame = Image.new('RGBA', image.size)
            frame.paste(image)

            frames.append(ImageQt.ImageQt(frame))

            image.seek(image.tell() + 1)
    except EOFError:
        pass

    return frames


# Locate save files:
def check_for_saves():
    if path.isdir('saves/'):
        for _, _, files in walk('saves/'):
            for file in files:
                if file.endswith('.buddy'):
                    return file


# Buddy file:
class BuddyFile:
    def __init__(self, name='', profile_path='', buddy_path=''):
        self.profile_picture = BuddyFile.determine_file_type(profile_path)
        self.buddy_picture = BuddyFile.determine_file_type(buddy_path)
        self.name = name

    @staticmethod
    def determine_file_type(filepath):
        image_reader = QImageReader(filepath)
        if image_reader.supportsAnimation() and image_reader.imageCount() > 1:
            return convert_gif_into_frames(filepath)
        else:
            return QImage(filepath)


# Buddy Serialization:
def write_buddy_images(out, picture):
    if isinstance(picture, QImage):
        out.writeInt8(0x0A)
        _ = out << picture

    elif isinstance(picture, list):
        mini_buddy_frame_size = len(picture)

        out.writeInt8(0x0B)
        out.writeInt16(mini_buddy_frame_size)
        for frame in picture:
            _ = out << frame


def save_buddy(buddy_file: BuddyFile, filename):
    if not path.isdir(f'./saves/{filename}'):
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
    write_buddy_images(out, buddy_file.profile_picture)

    # Buddy Picture(s):
    write_buddy_images(out, buddy_file.buddy_picture)

    file.close()


# Buddy Deserialization:
def load_buddy_images(in_file):
    image_type = in_file.readInt8()

    if image_type == 0x0A:
        image = QImage()
        in_file >> image

    elif image_type == 0x0B:
        frame_count = in_file.readInt16()
        image = []
        for _ in range(frame_count):
            temp_image = QImage()
            in_file >> temp_image

            image.append(temp_image)
    else:
        raise Exception('Buddy type not found.')

    return image


def load_buddy(filename=None):
    if not filename:
        filename = check_for_saves()
        if not filename:
            return

    filename = filename.replace('.buddy', '')

    # Deserializing:
    file = QFile(f"./saves/{filename}/{filename}.buddy")
    file.open(QIODevice.ReadOnly)

    # Stream & Magic Number & Version:
    in_file = QDataStream(file)
    magic = in_file.readInt32()

    if not magic == 0x0000C0D1:
        raise Exception('Version or validation number mismatch.')

    # Name:
    name = in_file.readString()

    # Profile Picture:
    profile_image = load_buddy_images(in_file)

    # Buddy Picture:
    buddy_image = load_buddy_images(in_file)

    return {'name': name, 'profile_picture': profile_image, 'mini_buddy_picture': buddy_image}


# Icon Serialization:
def save_icons(filepath):
    file = QFile(filepath)
    file.open(QIODevice.WriteOnly)

    # Stream & Magic Number & Version:
    out = QDataStream(file)
    out.writeInt32(0x0000C0D1)

    # Amount of icons:
    out.writeInt16(len([icon for icon in listdir('.') if path.isfile(icon)]))

    # Writing all icons:
    for icon_path, _, files in walk('./res/'):
        for f in files:
            if f.endswith('.png'):
                out.writeString(f.replace('.png', ''))
                out << QImage(icon_path + f)

    file.close()


# Icon Deserialization:
def load_icon(in_file):
    icon_name = in_file.readString()

    image = QImage()
    in_file >> image

    return icon_name, image


def load_icons(filepath=None):
    file = QFile(filepath)
    file.open(QIODevice.ReadOnly)

    # Stream & Magic Number & Version:
    in_file = QDataStream(file)
    magic = in_file.readInt32()

    if not magic == 0x0000C0D1:
        raise Exception('Version or validation number mismatch.')

    icons = {}
    file_amount = in_file.readInt16()

    for _ in range(file_amount):
        icon_name, icon = (load_icon(in_file))
        icons[icon_name] = icon

    return icons
