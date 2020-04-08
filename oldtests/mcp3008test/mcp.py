import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0]) # ilk bit channel, ikinci bit input, ucuncu bit DontCare
    data = ((adc[1]&3) << 8) + adc[2] # 1023 max bu yuzden 3 ile and operator u kullanilir ve kalan percentage adc[2] den eklenir
    print("")
    print(adc) # geri donen 3 lu bitten , ilki onemsiz, ikinci bitmask ile 8 bit lik kismi, ucuncu ise kalan son 8bit
    return data # 0-1023 arasi bir deger donderecektir
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,places)
    return volts

# Define sensor channels
# light_channel = 2
temp_channel  = 1
 
# Define delay between readings
delay = 2
 
while True:
 
    # Read the light sensor data
    # light_level = ReadChannel(light_channel)
    # light_volts = ConvertVolts(light_level,3)
    
    # Read the temperature sensor data
    temp_level = ReadChannel(temp_channel)
    temp_volts = ConvertVolts(temp_level,2)
    #   temp       = ConvertTemp(temp_level,2)
    
    # Print out results
    print "--------------------------------------------"
    # print("Gas: {} ({}V)".format(light_level,light_volts))
    print("Light : {} ({}V) ".format(temp_level,temp_volts))
    
    # Wait before repeating loop
    time.sleep(delay)