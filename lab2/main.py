from lab_python_oop.rectangle import rectangle
from lab_python_oop.Circle  import Circle
from lab_python_oop.square import Square


def main():
    r = rectangle("синего", 6, 2)
    c = Circle("зеленого", 10)
    s = Square("красного", 4)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
