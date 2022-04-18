# -*- coding: UTF-8 -*-

from pynput.mouse import Controller, Button, Listener


class Mouse(object):

    @staticmethod
    def on_move(x: int, y: int):
        print(f"Pointer moved to: {(x, y)}")

    @staticmethod
    def on_click(x: int, y: int, btn: Button, pressed: bool):
        print(f"{btn} {('pressed' if pressed else 'released')} at: {(x, y)}")
        if not pressed:
            # Stop the listener.
            return False

    @staticmethod
    def on_scroll(x: int, y: int, dx: int, dy: int):
        print(f"Scrolled {('down' if dy < 0 else 'up')} at: {(x, y)}")

    def __init__(self):
        self.ctrl = Controller()
        self.btn = Button

    @property
    def position(self) -> tuple:
        """Pointer (horizontal, vertical) position getter."""
        return self.ctrl.position

    @position.setter
    def position(self, value: tuple):
        """Pointer (horizontal, vertical) position setter."""
        self.ctrl.position = value

    def move(self, x: int, y: int):
        """
        Move the mouse pointer a number of pixels from its current position.

        :param x: The horizontal offset.
        :param y: The vertical offset.
        :raises ValueError: If the values are invalid, for example out of bounds.
        """
        self.ctrl.move(x, y)

    def click(self, btn: Button):
        """
        Emits a button press & release event at the current position.

        :param btn: The mouse button to be used.
        """
        self.ctrl.press(btn)
        self.ctrl.release(btn)

    def double_click(self):
        """
        Emits a double click event at the current position.
        The default implementation sends 2 series of pres & release events.
        """
        self.ctrl.click(self.btn.left, 2)

    def scroll(self, x: int, y: int):
        """
        Sends scroll events.

        :param x: The horizontal scroll.
        :param y: The vertical scroll.
        :raises ValueError: If the values are invalid, for example out of bounds.
        """
        self.ctrl.scroll(x, y)

    def listen(self):
        """Listen & collect mouse events until released."""
        with Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()
