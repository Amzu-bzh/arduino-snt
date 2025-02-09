# Documentation

This documentation is for the 1.0.0 version of arduino-snt. If you use a nearest version of the project and you don't find what you are searching for in this document, please open an issue on the project.

If at any time, you've an error while using the package, let's see the lest section of the documentation or share your issue ont the github projects page.

## Download

Go to the terminal and enter the follwoings commands :
```
pip install arduino-snt
```

## Blink a led

First, import the module.
``` python
import arduinoSNT
```

Next, declare your variables (board, LEDs, buttons, ect...) and start the iterator of the board.
``` python
board = arduinoSNT.Board("8") # Enter the bort of the arduino port (ex: COM8)
board.start()

led = board.create_led(13) # Enter the pin of the led
```

And finally, write the loop with the instructions for the components.
``` python
while True:
    led.turn_on()
    sleep(1)
    led.turn_off()
    sleep(1)
```

## Other components

### Button

To init a button, it's pretty similar as for the LED :
``` python
button = board.create_button(2)
```

If you want to know the state of the button you can use the methods : `.is_pressed()` and `.is_released()` which return a boolean.
