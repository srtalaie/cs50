import random
import sys

from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()


def fig_generator(s, f=None):
    if f is None:
        random_number = random.randint(0, len(fonts))
        figlet.setFont(font=fonts[random_number])
        return figlet.renderText(s)
    else:
        figlet.setFont(font=f)
        return figlet.renderText(s)


if len(sys.argv) == 1:
    str = input("Input: ")
    print(fig_generator(str))
elif (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and (sys.argv[2] in fonts)
):
    str = input("Input: ")
    print(fig_generator(str, sys.argv[2]))
else:
    sys.exit("Invalid usage")
