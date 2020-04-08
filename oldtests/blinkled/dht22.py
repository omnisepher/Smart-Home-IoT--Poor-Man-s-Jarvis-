import Adafruit_DHT
import sys

sensor = Adafruit_DHT.DHT22

pin = 14

humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)

if humidity is not None and temperature is not None:
	print ('{0:0.2f}'.format(temperature))
	print('{0:0.2f}'.format(humidity))


else:
	print('Failed to read')
