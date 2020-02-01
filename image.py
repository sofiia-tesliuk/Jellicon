#  Created by Sofiia Tesliuk at 2019-09-29.
import os
from PIL import Image


class UnImage:
    icon_sizes = [(16, 16),
                  (32, 32),
                  (64, 64),
                  (128, 128),
                  (256, 256),
                  (512, 512),
                  (1024, 1024)]

    @staticmethod
    def valid_format(image_filename):
        try:
            return image_filename.lower().split('.')[-1] in ['png', 'jpg', 'jpeg']
        except (IndexError, TypeError):
            return False

    @staticmethod
    def cut_image_name(image_path):
        return os.path.basename(image_path)

    @staticmethod
    def create_icns(path, image, icon_name):
        return UnImage._create_icon(path, image, icon_name, 'icns')

    @staticmethod
    def create_ico(path, image, icon_name):
        return UnImage._create_icon(path, image, icon_name, 'ico')

    @staticmethod
    def _create_icon(new_path, image_path, icon_name, extension):
        img = Image.open(image_path)
        img = UnImage._add_transparent_background(img)
        try:
            icon_filename = '{}.{}'.format(icon_name, extension)
        except IndexError:
            icon_filename = 'icon.{}'.format(extension)
        img.save('{}/{}'.format(new_path, icon_filename), sizes=UnImage.icon_sizes)
        return icon_filename

    @staticmethod
    def _add_transparent_background(image):
        # Resize image that it would fit 1024*1024 square
        width, height = image.size
        width_coefficient = 1
        height_coefficient = 1
        if width < height:
            width_coefficient = width / height
        elif height < width:
            height_coefficient = height / width
        image = image.resize((int(1024 * width_coefficient), int(1024 * height_coefficient)))
        width, height = image.size

        # Add image on transparent square 1024*1024
        tmp = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
        offset = ((1024 - width) // 2, (1024 - height) // 2)
        tmp.paste(image, offset)
        return tmp
