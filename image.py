#  Created by Sofiia Tesliuk at 2019-09-29.
from PIL import Image
from io import BytesIO


class ImageProcessor:
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
    def _icon_filename(image, extension):
        try:
            icon_filename = '{}.{}'.format(image.filename.split('.')[0], extension)
        except IndexError:
            icon_filename = 'icon.{}'.format(extension)
        return icon_filename

    @staticmethod
    def create_ico(image):
        return ImageProcessor._create_icon(image, 'ICO'), ImageProcessor._icon_filename(image, 'ico')

    @staticmethod
    def create_icns(image):
        return ImageProcessor._create_icon(image, 'ICNS'), ImageProcessor._icon_filename(image, 'icns')

    @staticmethod
    def _create_icon(image, format):
        img = Image.open(image)
        img = ImageProcessor._add_transparent_background(img)

        imagefile = BytesIO()
        img.save(imagefile, format=format, sizes=ImageProcessor.icon_sizes)
        imagefile.seek(0)
        return imagefile

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
