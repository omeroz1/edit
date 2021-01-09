from PIL import Image


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


image_path = 'deni.jpg'
image = read_image(image_path)


def change_to_red(image, level):
    """
        changes the color of the photo.
        :param level: the level of color in the picture. variable must be 1,2 or 3.
        :param image: the image given
        """
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

    if level is 1:
        selected_color = rl
    if level is 2:
        selected_color = rm
    if level is 3:
        selected_color = rs
    else:
        print("ERROR. level value can be: 1,2,3")
    updated_image = image.convert("RGB", selected_color)
    updated_image.show()


def change_to_green(image, level):
    """
        changes the color of the photo.
        :param level: the level of color in the picture. variable must be 1,2 or 3.
        :param image: the image given
        """
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

    if level is 1:
        selected_color = gl
    if level is 2:
        selected_color = gm
    if level is 3:
        selected_color = gs
    else:
        print("ERROR. level value can be: 1,2,3")
    updated_image = image.convert("RGB", selected_color)
    updated_image.show()


def change_to_blue(image, level):
    """
        changes the selected_color of the photo.
        :param level: the level of selected_color in the picture. variable must be 1,2 or 3.
        :param image: the image given
        """
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

    if level is 1:
        selected_color = bl
    if level is 2:
        selected_color = bm
    if level is 3:
        selected_color = bs
    else:
        print("ERROR. level value can be: 1,2,3")
    updated_image = image.convert("RGB", selected_color)
    updated_image.show()


def change_to_tourq(image, level):
    """
        changes the selected_color of the photo.
        :param level: the level of selected_color in the picture. variable must be 1,2 or 3.
        :param image: the image given
        """
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

    if level is 1:
        selected_color = tl
    if level is 2:
        selected_color = tm
    if level is 3:
        selected_color = ts
    else:
        print("ERROR. level value can be: 1,2,3")
    updated_image = image.convert("RGB", selected_color)
    updated_image.show()


def change_to_yellow(image, level):
    """
        changes the selected_color of the photo.
        :param level: the level of selected_color in the picture. variable must be 1,2 or 3.
        :param image: the image given
        """
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

    if level is 1:
        selected_color = yl
    if level is 2:
        selected_color = ym
    if level is 3:
        selected_color = ys
    else:
        print("ERROR. level value can be: 1,2,3")
    updated_image = image.convert("RGB", selected_color)
    updated_image.show()


def change_to_purple(image, level):
    """
    changes the selected_color of the photo.
    :param level: the level of selected_color in the picture. variable must be 1,2 or 3.
    :param image: the image given
    """
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

    if level is 1:
        selected_color = pl
    if level is 2:
        selected_color = pm
    if level is 3:
        selected_color = ps
    else:
        print("ERROR. level value can be: 1,2,3")



change_image_color(image, 'blue', 3)