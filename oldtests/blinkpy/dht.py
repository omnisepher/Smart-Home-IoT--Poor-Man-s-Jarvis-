import Adafruit_DHT as dht
h,t = dht.read_retry(dht.DHT22,14)
print ('Temp={0:0.1f} C and Humidity={1:0.1f}%').format(t,h)
