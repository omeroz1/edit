import os
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np


def read_image(path):
    """
    :param path: the path of the image
    :return: the photo in the variable: 'image'
    """
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        print(e)


def save_image(image, name):
    if name.__contains__('.jpg') or name.__contains__('.png') or name.__contains__('.JPG') or name.__contains__('.PNG'):
        image.save(name)
    else:
        image.save("{}{}".format(name, '.jpg'))


def get_image_size(image):
    """
    :param image: the image given
    :return: image size in pixels
    """
    return image.size


def resize_image(image, height, width):
    """
    change the image's size, without changing the image ratio.
    :param image: the image given
    :param height: new height in pixels
    :param width:new width in pixels
    :return: new image
    """
    resized_image = image.resize((height, width))
    return resized_image


def resize_copy_to_file(max_pixel):
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


def crop_image(image, xtop, ytop, xbottom, ybottom):
    """
    crops the image.
    xtop & ytop = the top left cordinates (xtop, ytop)
    xbottom & ybottom = the bottom right cordinates (xbottom, ybottom)
    :param image: image given
    :return: a cropped image
    """
    cropped = image.crop((xtop, ytop, xbottom, ybottom))
    return cropped


def center_image(image):
    """
    finds the center of the image.
    xtop & ytop = the top left cordinates (xtop, ytop)
    xbottom & ybottom = the bottom right cordinates (xbottom, ybottom)
    :param image: image given
    :return: the pixels pf the center image
    """
    width, height = image.size
    xtop = width / 4
    ytop = height / 4
    xbottom = 3 * width / 4
    ybottom = 3 * height / 4
    return xtop, ytop, xbottom, ybottom


def rotate_image(image, angle):
    """
    rotates the image
    :param image: the image given
    :param angle: the angle to rotate the image
    :return: a rotated image
    """
    return image.rotate(angle)


def gray_image(image):
    """
    :return: gray image
    """
    grayscale = image.convert("L")
    return grayscale


def change_image_color(image, color, level):
    """
    changes the image to any color given with 3 different levels.
    :param image: the image given
    :param color: the dominant color of the new image. 'red' 'green' 'blue' 'turquoise' 'yellow' 'purple'
    :param level: the level of selected_color in the picture. variable must be 1,2 or 3.
    """
    global selected_color
    rl = (
        0.4, 0.4, 0.4, 0,
        0.1, 0.1, 0.1, 0,
        0.1, 0.1, 0.1, 0)

    rm = (
        0.5, 0.5, 0.5, 0,
        0.1, 0.1, 0.1, 0,
        0.1, 0.1, 0.1, 0)

    rs = (
        0.7, 0.7, 0.7, 0,
        0.1, 0.1, 0.1, 0,
        0.1, 0.1, 0.1, 0)

    gl = (
        0.1, 0.1, 0.1, 0,
        0.3, 0.3, 0.3, 0,
        0.1, 0.1, 0.1, 0)

    gm = (
        0.1, 0.1, 0.1, 0,
        0.5, 0.5, 0.5, 0,
        0.1, 0.1, 0.1, 0)

    gs = (
        0.1, 0.1, 0.1, 0,
        0.7, 0.7, 0.7, 0,
        0.1, 0.1, 0.1, 0)

    bl = (
        0.2, 0.2, 0.2, 0,
        0.2, 0.2, 0.2, 0,
        0.5, 0.5, 0.5, 0)

    bm = (
        0.2, 0.2, 0.2, 0,
        0.2, 0.2, 0.2, 0,
        0.9, 0.9, 0.9, 0)

    bs = (
        0.15, 0.15, 0.15, 0,
        0.15, 0.15, 0.15, 0,
        0.9, 0.9, 0.9, 0)

    tl = (
        0.5, 0.5, 0.5, 0,
        0.6, 0.6, 0.6, 0,
        0.6, 0.6, 0.6, 0)

    tm = (
        0.3, 0.3, 0.3, 0,
        0.6, 0.6, 0.6, 0,
        0.6, 0.6, 0.6, 0)

    ts = (
        0.1, 0.1, 0.1, 0,
        0.6, 0.6, 0.6, 0,
        0.6, 0.6, 0.6, 0)

    yl = (
        0.6, 0.6, 0.6, 0,
        0.6, 0.6, 0.6, 0,
        0.5, 0.5, 0.5, 0)

    ym = (
        0.6, 0.6, 0.6, 0,
        0.6, 0.6, 0.6, 0,
        0.3, 0.3, 0.3, 0)

    ys = (
        0.6, 0.6, 0.6, 0,
        0.6, 0.6, 0.6, 0,
        0.1, 0.1, 0.1, 0)

    pl = (
        0.6, 0.6, 0.6, 0,
        0.5, 0.5, 0.5, 0,
        0.6, 0.6, 0.6, 0)

    pm = (
        0.6, 0.6, 0.6, 0,
        0.3, 0.3, 0.3, 0,
        0.6, 0.6, 0.6, 0)

    ps = (
        0.6, 0.6, 0.6, 0,
        0.1, 0.1, 0.1, 0,
        0.6, 0.6, 0.6, 0)

    if color == 'red':
        if level == 1:
            selected_color = rl
        if level == 2:
            selected_color = rm
        if level == 3:
            selected_color = rs
        else:
            print("ERROR. level value can be: 1,2,3")
    if color == 'green':
        if level == 1:
            selected_color = gl
        if level == 2:
            selected_color = gm
        if level == 3:
            selected_color = gs
        else:
            print("ERROR. level value can be: 1,2,3")
    if color == 'blue':
        if level == 1:
            selected_color = bl
        if level == 2:
            selected_color = bm
        if level == 3:
            selected_color = bs
        else:
            print("ERROR. level value can be: 1,2,3")
    if color == 'turquoise':
        if level == 1:
            selected_color = tl
        if level == 2:
            selected_color = tm
        if level == 3:
            selected_color = ts
        else:
            print("ERROR. level value can be: 1,2,3")
    if color == 'yellow':
        if level == 1:
            selected_color = yl
        if level == 2:
            selected_color = ym
        if level == 3:
            selected_color = ys
        else:
            print("ERROR. level value can be: 1,2,3")
    if color == 'purple':
        if level == 1:
            selected_color = pl
        if level == 2:
            selected_color = pm
        if level == 3:
            selected_color = ps
        else:
            print("ERROR. level value can be: 1,2,3")

    updated_image = image.convert("RGB", selected_color)
    return updated_image


def comix_image(image):
    """
    :return: comix image
    """
    comix = image.convert("P")
    return comix


def bw_image(image, threshold):
    """
    convert the image to black & white
    :param image: image given
    :param threshold: bigger value -> more black.
                      lower value -> more white.
    :return: binary image
    """
    gray = gray_image(image)
    arr = np.array(gray)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] >= threshold:
                arr[i][j] = 255
            else:
                arr[i][j] = 0
    return Image.fromarray(arr)


def flip_image(image):
    img_array = np.array(image)
    img_flipped_data = np.flip(img_array, axis=1)
    img_flipped = Image.fromarray(img_flipped_data)
    img_flipped.show()


def brightness_image(image):
    enhancer = ImageEnhance.Brightness(image)
    img_light = enhancer.enhance(0.5)
    img_light.show()

def contrast_image(image):
    enhancer = ImageEnhance.Contrast(image)
    updated_img = enhancer.enhance(0.5)
    updated_img.show()


def sharpness_image(image):
    enhancer = ImageEnhance.Sharpness(image)
    updated_img = enhancer.enhance(1.5)
    updated_img.show()


def more_color_image(image):
    enhancer = ImageEnhance.Color(image)
    updated_img = enhancer.enhance(1.5)
    updated_img.show()

if __name__ == '__main__':
    image_path = 'deni.jpg'
    image = read_image(image_path)
    # image.show()
    img_array = np.array(image)
    # print(img_array)
    # print(get_image_size(image))
    # cropped = crop_image(image, 100, 100, 100, 100)
    # cropped.show()
    """center = center_image(image)
    xtop, ytop, xbottom, ybottom = center
    print(center)
    print(get_image_size(image))
    center_cropped = crop_image(image, 0, 0, 100, 250)
    center_cropped.show()"""
    # print(img_array.shape)
    # gray = gray_image(image)
    # gray.show()
    """bw_photo = bw_image(image, 100)
    bw_photo.show()
   colored = change_image_color(image, 'green', 3)
    colored.show()
   edges = image.filter(ImageFilter.FIND_EDGES)
    bands = edges.split()
    outline = bands[0].point(lambda x:255 if x<100 else 0)
    outline.show()"""
    # flip_image(image)
    #brightness_image(image)
    # contrast_image(image)
    #color_image(image)