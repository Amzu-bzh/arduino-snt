import pyfirmata

from .board import Board


class Button:
    def __init__(self, board: Board, pin: int) -> None:
        try:
            self.pin = pin
            self.button = board.board.digital[pin]
            self.button.mode = pyfirmata.INPUT
        except:
            print("An error as occurred during the instantiation of the class Button.")
            quit()

    def get_pin(self) -> int:
        return self.pin

    def is_pressed(self) -> bool:
        return self.button.read()