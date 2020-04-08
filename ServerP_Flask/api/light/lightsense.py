import spidev
import RPi.GPIO as GPIO
import time
import os

lightled = 40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(lightled, GPIO.OUT, initial=GPIO.LOW)

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

# SPI data from MCP3008 chip as 2**10
# Inputs are 0-7


def readInput(channel):
    # ilk bit channel, ikinci bit input, ucuncu bit DontCare
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    # 1023 max bu yuzden 3 ile and operator u kullanilir ve kalan percentage adc[2] den eklenir
    data = ((adc[1] & 3) << 8) + adc[2]
    # print(adc)  # geri donen 3 lu bitten , ilki onemsiz, ikinci bitmask ile 8 bit lik kismi, ucuncu ise kalan son 8bit
    return data  # 0-1023 arasi bir deger donderecektir


def showAsVolts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts


lightInput = 1

def read():
    light_level = readInput(lightInput)
    return light_level

def comset(command):
    if command == 1:
        GPIO.output(lightled, GPIO.HIGH)
    if command == 0:
        GPIO.output(lightled, GPIO.LOW)
