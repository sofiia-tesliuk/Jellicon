from PIL import Image
import glob
import os


icons = [('icon_512x512@2x.png', (1024, 1024)),
         ('icon_512x512.png',  (512, 512)),
         ('icon_256x256@2x.png', (512, 512)),
         ('icon_256x256.png',  (256, 256)),
         ('icon_128x128@2x.png', (256, 256)),
         ('icon_128x128.png',  (128, 128)),
         ('icon_32x32@2x.png',  (64, 64)),
         ('icon_32x32.png',   (32, 32)),
         ('icon_16x16@2x.png',  (32, 32)),
         ('icon_16x16.png',   (16, 16))]


def image_name():
    """
    :return: name of image (.png format) in directory image.
    """
    image_path = working_directory_path + '/image/'
    format_file = '*.png'
    images = glob.glob(image_path + format_file)
    if images:
        if len(images) > 1:
            raise ValueError('In directory images/ more than one image')
        else:
            return images[0]
    else:
        raise ValueError('Directory images/ is empty')


def icon_set(icon_dir):
    """
    :param icon_name: name of icon
    :creates: folder of scaled icons
    """
    im = Image.open(image_name())
    os.mkdir('{}/{}'.format(working_directory_path, icon_dir))
    for icon in icons:
        im = im.resize(icon[1])
        im.save('{}/{}/{}'.format(working_directory_path, icon_dir, icon[0]))


def commands_in_terminal(icon_dir):
    """
    Run some commands in terminal to create right icon
    :param icon_dir: name of directory with icons images
    """
    # os.system('cd {}/'.format(working_directory_path))
    os.system('iconutil -c icns {}'.format(icon_dir))
    os.system('rm -rf {}'.format(icon_dir))


def main():
    icon_name = input('Enter icon name: ')
    icon_directory = icon_name.replace(' ', '_') + '.iconset'
    try:
        icon_set(icon_directory)
        commands_in_terminal(icon_directory)
    except ValueError as err:
        print(err)
    except:
        print('Something gone wrong.')
    else:
        print('Done.')


if __name__ == "__main__":
    working_directory_path = os.path.dirname(os.path.abspath(__file__))
    main()
