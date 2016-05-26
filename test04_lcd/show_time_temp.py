import lcddriver
import datetime
from time import sleep, strftime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

lcd = lcddriver.lcd()

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        #str_temp = '{0:0.1f}*C'.format(temperature)

        ahora_dia  = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        ahora_hora = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')


        lcd.lcd_display_string(ahora_dia, 1)
        #lcd.lcd_display_string(str_temp, 1)
        second_line = ahora_hora + '{:7.1f}C'.format(temperature)
        print second_line
        #lcd.lcd_display_string(ahora_hora, 2)
        lcd.lcd_display_string(second_line, 2)

        sleep(1)
except KeyboardInterrupt:
    pass

lcd.lcd_clear()
