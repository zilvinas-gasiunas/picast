import RPi.GPIO as GPIO
from classes.chrome_cast import ChromeCast
from classes.input_pin import InputPin
from classes.video_id_provider import VideoIdProvider

GPIO.setmode(GPIO.BCM)

inPin1 = InputPin(4)
inPin2 = InputPin(17)
inPin3 = InputPin(18)
inPin4 = InputPin(23)

videoIdProvider = VideoIdProvider()
livingRoom = ChromeCast('Living Room TV')

try:
    while 1:
        if inPin1.isOn():
            print("Playing one")
            livingRoom.play(videoIdProvider.getVideo(1))

        if inPin2.isOn():
            print("Playing two")
            livingRoom.play(videoIdProvider.getVideo(2))

        if inPin3.isOn():
            print("Playing three")
            livingRoom.play(videoIdProvider.getVideo(3))

        if inPin4.isOn():
            print("Playing four")
            livingRoom.play(videoIdProvider.getVideo(4))

except KeyboardInterrupt:
    GPIO.cleanup()
