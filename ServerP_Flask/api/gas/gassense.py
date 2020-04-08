import RPi.GPIO as GPIO
from time import sleep

gaspin = 7
gasled = 38
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gaspin, GPIO.IN)  # pin7 is digital input of MQ
GPIO.setup(gasled, GPIO.OUT, initial=GPIO.LOW)

# while True:
#     print(GPIO.input(7))
#     sleep(0.1)


def read():
    return GPIO.input(gaspin)


def comset(command):
    if command == 1:
        GPIO.output(gasled, GPIO.HIGH)
    if command == 0:
        GPIO.output(gasled, GPIO.LOW)

