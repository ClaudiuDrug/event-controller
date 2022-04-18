# -*- coding: UTF-8 -*-

from typing import Union
from time import sleep
from eventctrl import Mouse
from random import choice

mouse = Mouse()
pointer: tuple = (0, 0)
byte_set: set = {
    "0000", "0001", "0010", "0011",
    "0100", "0101", "0110", "0111",
    "1000", "1001", "1010", "1011",
    "1100", "1101", "1110", "1111",
}


def bounce(steps: int = 0):
    global pointer, mouse

    mouse.listen()
    sleep(3)

    pointer = mouse.position
    step = 1

    while True:

        for item in range(steps):
            print(random_str(16))
            scroll(step)
            sleep(0.125)

        step = negate(step)


def random_str(length: int):
    global byte_set
    return " ".join(choice(list(byte_set)) for n in range(length))


def scroll(steps: int):
    global mouse, pointer

    if mouse.position != pointer:
        print(f"Cursor moved to: {mouse.position}")
        quit()

    mouse.scroll(0, steps)


def negate(value: Union[int, float]) -> Union[int, float]:
    return -value if (value > 0) else abs(value)


if __name__ == '__main__':
    bounce(10)
