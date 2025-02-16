class PinAlreadyUsedError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class PinNotUsedError(Exception):
    def __init__(self, message: str):
        super().__init__(message)