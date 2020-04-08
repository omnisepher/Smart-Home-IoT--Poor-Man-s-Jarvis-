import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(3) == GPIO.LOW:
        print("Button pushed")
        break