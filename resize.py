from PIL import Image
import os


def resize_file(max_pixel):
    """
    takes all of the photos in the directory and resizes them to the 'max_pixel' limit.
    :param max_pixel: the maximum length and width of the image.
    :return: the new image in a folder named after the number of the 'max_pixel' in the same directory.
    """
    path = os.getcwd()
    pix_size = (max_pixel, max_pixel)
    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            i = Image.open(f)
            iname, iend = os.path.splitext(f)
            print(iend)
            if os.path.exists(os.path.join(path, str(max_pixel))):
                i.thumbnail(pix_size)
                i.save('{}/{}_{}{}'.format(str(max_pixel), iname, str(max_pixel), iend))
            else:
                os.mkdir(os.path.join(path, str(max_pixel)))
                i.thumbnail(pix_size)
                i.save('{}/{}_{}{}'.format(str(max_pixel), iname, str(max_pixel), iend))


if __name__ == '__main__':
    resize_file(200)
