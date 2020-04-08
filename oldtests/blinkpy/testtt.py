import Adafruit_DHT
from time import sleep

sensor = Adafruit_DHT.DHT22

pin = 14

humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)

while 1:
    sleep(1)
    if humidity is not None and temperature is not None:
        print ('Temp={0:0.1f}*C and Humidity={1:0.1f}%'.format(temperature,humidity))
    else:
        print('Failed to read')
