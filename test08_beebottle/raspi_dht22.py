#!/usr/bin/env python

############################################################
# This code uses the Beebotte API, you must have an account.
# You can register here: http://beebotte.com/register
############################################################

import time
import Adafruit_DHT
from beebotte import *

### Replace API_KEY and SECRET_KEY with those of your account
#bbt = BBT('API_KEY', 'SECRET_KEY')
bbt = BBT('70528c7f91a673d3454886f1bc1e8797', 'beb76ecca27ed672a44d914ecb45326af7ed1921cdf7b9551ce1088ab74e55ad')

period = 300 ## Sensor data reporting period (5 minutes)
pin = 4 ## Assuming the DHT11 sensor is connected to GPIO pin number 4

### Change channel name and resource names as suits you
temp_resource   = Resource(bbt, 'RaspberryPi', 'temperature')
humid_resource  = Resource(bbt, 'RaspberryPi', 'humidity')

def run():
  while True:
    ### Assume
    humidity, temperature = Adafruit_DHT.read_retry( Adafruit_DHT.DHT22, pin )
    if humidity is not None and temperature is not None:
#        print "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity)
        try:
          #Send temperature to Beebotte
          temp_resource.write(temperature)
          #Send humidity to Beebotte
          humid_resource.write(humidity)
        except Exception:
          ## Process exception here
          print "Error while writing to Beebotte"
    else:
        print "Failed to get reading. Try again!"

    #Sleep some time
    time.sleep( period )

run()
