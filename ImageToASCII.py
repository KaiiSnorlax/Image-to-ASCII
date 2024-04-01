import math
import sys

from PIL import Image


def image_prompt():

    while True:
        path = input("Enter the path to your image file: ").replace('"', "")
        try:
            img = Image.open(path)
            break
        except FileNotFoundError:
            print("Invalid image path! try again")
            continue
        except AttributeError:
            print("Invalid image path! try again")
            continue
    return img


def size_prompt():
    while True:
        maxsize = input("Enter how big you want it: ")
        try:
            maxsize = abs(int(maxsize))
            break
        except ValueError:
            print("Please type a whole number!")
            continue
    return maxsize


def light_bias_prompt():
    while True:
        light_bias = input("Enter a lightness bias ( larger number for lighter images, smaller number for darker images ): ")
        try:
            light_bias = abs(float(light_bias))
            break
        except ValueError:
            print("Please type a number!")
            continue
    return light_bias


def prepare_image():
    if len(sys.argv) < 2:
        img = image_prompt()
    else:
        try:
            img = Image.open(sys.argv[1].replace('"', ""))
        except:
            print("Invalid image")

    if len(sys.argv) < 3:
        maxsize = size_prompt()
    else:
        maxsize = int(sys.argv[2])

    if len(sys.argv) < 4:
        light_bias = light_bias_prompt()
    else:
        light_bias = float(sys.argv[3])

    if len(sys.argv) < 5:
        output_location = None
    else:
        output_location = sys.argv[4]

    img.thumbnail((maxsize, maxsize))

    return img, light_bias, output_location


def to_ascii(img, width, height, light_bias, min_val, max_val):
    art = ""
    for y in range(height):
        for x in range(width):
            my_tuple = img.getpixel((x, y))
            if my_tuple[1] == 0:
                art += "  "
            else:
                art += (pixel_brightness(my_tuple[0], min_val, max_val, light_bias) + " ")
        art += "\n"
    return art


def find_brightness_range(img, width, height):
    max_val = 0
    min_val = 255
    for y in range(height):
        for x in range(width):
            my_tuple = img.getpixel((x, y))
            if my_tuple[0] > max_val and my_tuple[1] != 0:
                max_val = my_tuple[0]
            elif my_tuple[0] < min_val and my_tuple[1] != 0:
                min_val = my_tuple[0]
    return min_val, max_val


def pixel_brightness(grayscale_value, min_val, max_val, bias):
    pixel = grayscale_value - min_val
    pixel /= (max_val - min_val)
    pixel = math.pow(pixel, bias)
    pixel *= (len(ASCII_CHAR_MAP) - 1)

    return ASCII_CHAR_MAP[math.ceil(pixel)]


ASCII_CHAR_MAP = "@&%QWNM0gB$#DR8mHXKAUbGOpV4d9h6PkqwSE2]ayjxY5Zoen[ult13If}C{iF|(7J)vTLs?z/*cr!+<>;=^,_:'-.` "


user_input = prepare_image()
user_image, lightness_bias, art_file = user_input[0], user_input[1], user_input[2]
image_width, image_height = user_image.size[0], user_image.size[1]


brightness_range = find_brightness_range(user_image.convert('LA'), image_width, image_height)
lightest_pixel, darkest_pixel = brightness_range[0], brightness_range[1]


ascii_art = to_ascii(user_image.convert('LA'), image_width, image_height, lightness_bias, lightest_pixel, darkest_pixel)

if art_file is None:
    print(ascii_art)
else:
    f = open(art_file, "w")
    f.write(ascii_art)
    f.close()
