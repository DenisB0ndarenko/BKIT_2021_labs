from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import Fore, Back, Style


def main():
    r = Rectangle("синего", 2, 2)
    c = Circle("зеленого", 2)
    s = Square("красного", 2)
    print(r)
    print(c)
    print(s)
    print(Fore.RED + 'some red text')
    print(Back.BLUE + 'and with a blue background')
    print(Style.RESET_ALL)
    print('some normal text')


if __name__ == "__main__":
    main()
