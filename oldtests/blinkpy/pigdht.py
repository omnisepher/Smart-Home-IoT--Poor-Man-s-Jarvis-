import DHT22
import pigpio
from time import sleep
import datetime
# this connects to the pigpio daemon which must be started first
pi = pigpio.pi()
# Pigpio DHT22 module should be in same folder as your program
s = DHT22.sensor(pi, 14)
s.trigger()
sleepTime = 3  # Necessary on faster Raspberry Pi's
def read():
    s.trigger()
    temp = round(s.temperature(),2)
    hum = round(s.humidity(),2)
    return (temp,hum)

while True:
    print(datetime.datetime.now().time())
    temX,humx = read()
    print(temX,humx)
    sleep(sleepTime)
# s.cancel()
# pi.stop()
