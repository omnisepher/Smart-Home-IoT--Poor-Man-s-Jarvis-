import RPi.GPIO as GPIO
from time import sleep

gaspin = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gaspin, GPIO.IN) #pin7 is digital input of MQ

# while True:
#     print(GPIO.input(7))
#     sleep(0.1)

def gasRead():
    return GPIO.input(gaspin)