import lcddriver
import datetime
from time import sleep, strftime
import Adafruit_DHT
from beebotte import *


sensor = Adafruit_DHT.DHT22
pin = 4

BEEBOTTLE_TIMEOUT = 300
counter = 0

bbt = BBT('70528c7f91a673d3454886f1bc1e8797', 'beb76ecca27ed672a44d914ecb45326af7ed1921cdf7b9551ce1088ab74e55ad')

temp_resource   = Resource(bbt, 'RaspberryPi', 'temperature')
humid_resource  = Resource(bbt, 'RaspberryPi', 'humidity')

lcd = lcddriver.lcd()

try:
    while True:
        counter += 1
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        ahora_dia  = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        ahora_hora = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')

        lcd.lcd_display_string(ahora_dia, 1)
        lcd.lcd_display_string(ahora_hora + '{:7.1f}C'.format(temperature), 2)
        sleep(1)
        if counter == BEEBOTTLE_TIMEOUT:
            try:
                #Send temperature to Beebotte
                temp_resource.write(temperature)
                #Send humidity to Beebotte
                humid_resource.write(humidity)
                counter = 0
            except Exception:
                ## Process exception here
                print "Error while writing to Beebotte"

except KeyboardInterrupt:
    pass

lcd.lcd_clear()
