import RPi.GPIO as GPIO


class InputPin:

    # Initializer / Instance Attributes
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_UP)

    def isOn(self):
        return GPIO.input(self.pin)
