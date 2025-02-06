import pyfirmata

class Board:
    def __init__(self, port) -> None:
        try:
            self.port = f"COM{port}"
            self.board = pyfirmata.Arduino(self.port)

        except:
            print("An error as occurred during the instantiation of the class Board.")
            quit()

    def get_port(self) -> str:
        return self.port