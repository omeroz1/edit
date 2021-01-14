import os
import PIL.Image
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageTk
import numpy as np
from tkinter import *
import datetime
from functools import partial


def read_image(path):
    """
    :param path: the path of the image
    :return: the photo in the variable: 'image'
    """
    global ID
    try:
        image = PIL.Image.open(path)
        date = datetime.datetime.now()
        ID = date.strftime('%d') + date.strftime('%m') + date.strftime('%H') + date.strftime('%M')
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
    resized_image = image.resize((height, width), PIL.Image.ANTIALIAS)
    return resized_image


def get_image_info(image):
    for f in os.listdir('.'):
        if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.JPG') or f.endswith('.PNG'):
            i = read_image(f)
            if i.size == image.size:
                iname, iend = os.path.splitext(f)
                return iname, iend


def save_to_dir(image):
    path = os.getcwd()
    iname, iend = get_image_info(image)
    if os.path.exists(os.path.join(path, str(ID))):
        image.save('{}/{}_{}{}'.format(str(ID), iname, str(ID), iend))
    else:
        os.mkdir(os.path.join(path, str(ID)))
        image.save('{}/{}_{}{}'.format(str(ID), iname, str(ID), iend))


def copy_all_to_file():
    """
    copy the image to the directory named after the image ID.
    example: 'deni.jpg' will be 'deni_ID.jpg'
    """
    path = os.getcwd()
    for f in os.listdir('.'):
        if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.JPG') or f.endswith('.PNG'):
            i = PIL.Image.open(f)
            iname, iend = os.path.splitext(f)
            if os.path.exists(os.path.join(path, str(ID))):
                i.save('{}/{}_{}{}'.format(str(ID), iname, str(ID), iend))
            else:
                os.mkdir(os.path.join(path, str(ID)))
                i.save('{}/{}_{}{}'.format(str(ID), iname, str(ID), iend))


def crop_image(image, xtop, ytop, xbottom, ybottom):
    """
    crops the image.
    xtop & ytop = the top left cordinates (xtop, ytop)
    xbottom & ybottom = the bottom right cordinates (xbottom, ybottom)
    :param image: image given
    :return: a cropped image
    """
    cropped = image.crop((xtop, ytop, xbottom, ybottom))
    save_to_dir(cropped)
    cropped.show()


def get_center_image(image):
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
    updated_image = image.rotate(angle)
    save_to_dir(updated_image)
    updated_image.show()


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
        elif level == 2:
            selected_color = rm
        elif level == 3:
            selected_color = rs
        else:
            print("ERROR. level value can be: 1,2,3")
    elif color == 'green':
        if level == 1:
            selected_color = gl
        elif level == 2:
            selected_color = gm
        elif level == 3:
            selected_color = gs
        else:
            print("ERROR. level value can be: 1,2,3")
    elif color == 'blue':
        if level == 1:
            selected_color = bl
        elif level == 2:
            selected_color = bm
        elif level == 3:
            selected_color = bs
        else:
            print("ERROR. level value can be: 1,2,3")
    elif color == 'turquoise':
        if level == 1:
            selected_color = tl
        elif level == 2:
            selected_color = tm
        elif level == 3:
            selected_color = ts
        else:
            print("ERROR. level value can be: 1,2,3")
    elif color == 'yellow':
        if level == 1:
            selected_color = yl
        elif level == 2:
            selected_color = ym
        elif level == 3:
            selected_color = ys
        else:
            print("ERROR. level value can be: 1,2,3")
    elif color == 'purple':
        if level == 1:
            selected_color = pl
        elif level == 2:
            selected_color = pm
        elif level == 3:
            selected_color = ps
        else:
            print("ERROR. level value can be: 1,2,3")
    if color == 'red' or color == 'green' or color == 'blue' or color == 'turquoise' or color == 'orange' \
            or color == 'purple':
        updated_image = image.convert("RGB", selected_color)
        save_to_dir(updated_image)
        updated_image.show()
    else:
        if color == 'grey' or color == 'gray':
            grayscale = image.convert("L")
            save_to_dir(grayscale)
            grayscale.show()

        else:
            print("ERROR. color not found. color can be: red, green, blue, turquoise, orange, purple or grey")


def comix_image(image):
    """
    :return: comix image
    """
    comix = image.convert("P")
    comix.show()


def gray_image(image):
    grayscale = image.convert("L")
    return grayscale


def bw_image(image, hardness):
    """
    convert the image to black & white
    :param image: image given
    :param hardness: bigger value -> more black.
                      lower value -> more white.
    :return: binary image
    """
    gray = gray_image(image)
    arr = np.array(gray)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] >= hardness:
                arr[i][j] = 255
            else:
                arr[i][j] = 0
    PIL.Image.fromarray(arr).show()


def flip_image(image):
    """
    flips the image
    """
    img_array = np.array(image)
    img_flipped_data = np.flip(img_array, axis=1)
    img_flipped = PIL.Image.fromarray(img_flipped_data)
    img_flipped.show()


def brightness_image(image):
    """
    increase or decrese the brightness.
    img_light > 1 = brighter
    img_light < 1 = darker
    """
    enhancer = ImageEnhance.Brightness(image)
    img_light = enhancer.enhance(3)
    save_to_dir(img_light)
    img_light.show()


def contrast_image(image):
    """
    increase or decrese the contrast.
    updated_img > 1 = more contrast
    updated_img < 1 = less contrast
    """
    enhancer = ImageEnhance.Contrast(image)
    updated_img = enhancer.enhance()
    save_to_dir(updated_img)
    updated_img.show()


def sharpness_image(image):
    """
    increase or decrese the sharpness.
    updated_img > 1 = more sharpness
    updated_img < 1 = less sharpness
    """
    enhancer = ImageEnhance.Sharpness(image)
    updated_img = enhancer.enhance(5)
    save_to_dir(updated_img)
    updated_img.show()


def more_color_image(image):
    """
    increase or decrese the color.
    updated_img > 1 = more color
    updated_img < 1 = less color
    """
    enhancer = ImageEnhance.Color(image)
    updated_img = enhancer.enhance(1.5)
    updated_img.show()


if __name__ == '__main__':
    image_path = 'deni.jpg'
    image = read_image(image_path)
    contrast_image(image)