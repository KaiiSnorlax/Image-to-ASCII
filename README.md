# Image to Ascii

## Description
Converts a bitmap image into ASCII art.

Chosen bitmap image goes through two big changes, gets resized based off a maximum size of your choice, then converted into grayscale. Based off pixels value and light bias outputs a character based on the brightness of the pixel.

## Dependencies 
- [Python 3](https://www.python.org/downloads/)
- [Pillow](https://pypi.org/project/pillow/)

## Usage
Run the following command in the root directory of the source.

`python ImageToASCII.py bitmap_image_path maxsize lightbias [text_file_path]`

- bitmap_image_path : path to input image
- maxsize : the size you want your ASCII art to be
- lightbias : choose a number, larger number for light images, smaller number for darker images (Reccomended less than 1)
- text_file_path : path to text file, if not specified will default stdout