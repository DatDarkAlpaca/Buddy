from PySide6.QtGui import QImageReader, QPixmap, QImage
from PySide6.QtCore import QFile, QIODevice, QDataStream
from zipfile import ZipFile
from os import path, listdir, remove, getcwd
from PIL import Image


# Locate saves:
def check_for_saves():
    if path.isdir('./saves/'):
        for file in listdir('./saves/'):
            if file.endswith('.cif'):
                return './saves/' + file


# Buddy file:
class BuddyFile:
    def __init__(self, name='', profile_path='', buddy_path=''):
        self.is_profile_image, self.is_buddy_image = [True] * 2

        # Profile Picture:
        image_reader = QImageReader(profile_path)
        if image_reader.supportsAnimation() and image_reader.imageCount() > 1:
            self.is_profile_image = False
        else:
            self.profile_picture = QPixmap(profile_path)

        # Mini Buddy Picture:
        image_reader = QImageReader(profile_path)
        if image_reader.supportsAnimation() and image_reader.imageCount() > 1:
            self.is_buddy_image = False
        else:
            self.buddy_picture = QPixmap(buddy_path)

        self.profile_picture_path, self.buddy_picture_path = profile_path, buddy_path
        self.name = name


# Saving:
# Todo: reduce.
def save_buddy(buddy_file: BuddyFile, filename):
    file = QFile(f"./saves/{filename}.ii")
    file.open(QIODevice.WriteOnly)

    # Stream & Magic Number & Version:
    out = QDataStream(file)
    out.writeInt32(0x0000C0D1)

    # Name:
    out.writeString(buddy_file.name)

    # Profile Picture:
    profile_resource = None
    if buddy_file.is_profile_image:
        out.writeInt8(True)
        out << buddy_file.profile_picture.toImage()
    else:
        out.writeBool(False)
        profile_resource = Image.open(buddy_file.profile_picture_path)

    # Mini Buddy Picture:
    mini_buddy_resource = None
    if buddy_file.is_buddy_image:
        out.writeBool(True)
        out << buddy_file.buddy_picture.toImage()
    else:
        out.writeBool(False)
        mini_buddy_resource = Image.open(buddy_file.buddy_picture_path)

    file.close()

    # Zipping:
    with ZipFile(f"./saves/{buddy_file.name}.cif", 'w') as zip_file:
        zip_file.write(f"./saves/{filename}.ii", f"{filename}.ii")
        remove(f"./saves/{filename}.ii")

        if profile_resource:
            profile_resource.save('./saves/profile.gif', save_all=True)
            profile_resource.close()
            zip_file.write('./saves/profile.gif')

        if mini_buddy_resource:
            mini_buddy_resource.save('./saves/buddy.gif', save_all=True)
            mini_buddy_resource.close()
            zip_file.write('./saves/buddy.gif')


# Load:
def load_buddy(filepath):
    name = ''
    profile_image = None
    buddy_image = None

    # Unzip:
    with ZipFile(filepath, 'r') as zip_file:
        zip_file.extractall(getcwd() + '/saves/')

        for file in listdir(getcwd() + '/saves/'):
            if file.endswith('ii'):
                q_file = QFile(getcwd() + '/saves/' + file)
                q_file.open(QIODevice.ReadOnly)

                # Stream & Magic Number & Version:
                in_file = QDataStream(q_file)

                magic = in_file.readInt32()
                if magic != 0x0000C0D1:
                    raise Exception('Bad file format.')

                # Name:
                name = in_file.readString()

                # Profile Picture:
                exists_profile = in_file.readBool()

                if exists_profile:
                    profile_image = QImage()
                    in_file >> profile_image

                # Buddy Picture:
                exists_buddy = in_file.readBool()

                if exists_buddy:
                    buddy_image = QImage()
                    in_file >> buddy_image

                q_file.close()

                remove(getcwd() + '/saves/' + file)

            if file == 'profile.gif':
                profile_image = getcwd() + '/saves/' + 'profile.gif'

            if file == 'buddy.gif':
                buddy_image = getcwd() + '/saves/' + 'buddy.gif'

    return {'name': name, 'profile_picture': profile_image, 'mini_buddy_picture': buddy_image}
