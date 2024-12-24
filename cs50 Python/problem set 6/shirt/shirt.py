import os
import sys

from PIL import Image, ImageOps

extensions = [".jpg", ".jpeg", ".png"]


def file_extension_check(string, substrings):
    file = os.path.splitext(string)
    string_lower = file[1].lower()
    if string_lower not in substrings:
        return True
    return False


def file_extension_same_check(file_1, file_2):
    file_1_list = os.path.splitext(file_1)
    file_1_ext = file_1_list[1]
    file_2_list = os.path.splitext(file_2)
    file_2_ext = file_2_list[1]

    if file_1_ext.lower() != file_2_ext.lower():
        return True
    else:
        return False


try:
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif file_extension_check(sys.argv[1], extensions):
        sys.exit("Invalid input")
    elif file_extension_check(sys.argv[2], extensions):
        sys.exit("Invalid output")
    elif file_extension_same_check(sys.argv[1], sys.argv[2]):
        sys.exit("Input and output have different extensions")
    else:
        with open(sys.argv[1]) as file:
            input = Image.open(sys.argv[1])
            input = ImageOps.fit(input, shirt_size)
            input.paste(shirt, box=(0, 0), mask=shirt)
            input.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
