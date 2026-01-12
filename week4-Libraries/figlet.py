import pyfiglet
import random
import sys
fonts=["standard",
    "slant",
    "3-d",
    "3x5",
    "5lineoblique",
    "alphabet",
    "banner",
    "bubble",
    "bulbhead",
    "digital",
    "doh",
    "doom",
    "isometric1",
    "larry3d",
    "letters",
    "nancyj",
    "starwars",
    "stop",
    "smscript",
    "smshadow"]

def main():
    try:
        if not sys.argv[1]=="-f" or sys.argv[1]=="--font" or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        else:
            user_input=input("input:")
            f=sys.argv[2]
            print(pyfiglet.figlet_format(user_input, font=f))
    except IndexError:
        user_input=input("input:")
        print(pyfiglet.figlet_format(user_input, font=random.choice(fonts)))

main()