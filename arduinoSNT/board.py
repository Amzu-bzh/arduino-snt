import pyfirmata
import pyfirmata.util

from .button import Button
from .led import Led

class Board:
    def __init__(self, port) -> None:
        try:
            self.port = f"COM{port}"
            self.board = pyfirmata.Arduino(self.port)

            self.iterator = pyfirmata.util.Iterator(self.board)

        except Exception as e:
            print(f"An error as occurred during the instantiation of the class Board:\n{e}")
            quit()

    def start(self) -> None:
        self.iterator.start()

    def get_port(self) -> str:
        return self.port

    def create_button(self, pin: int) -> Button:
        return Button(self, pin)

    def create_led(self, pin: int) -> Led:
        return Led(self, pin)