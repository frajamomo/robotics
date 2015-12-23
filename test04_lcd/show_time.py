import lcddriver
from time import *
import datetime

lcd = lcddriver.lcd()

try:
    while True:
        ahora_dia  = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        ahora_hora = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
        lcd.lcd_display_string(ahora_dia, 1)
        lcd.lcd_display_string(ahora_hora, 2)
        sleep(1)
except KeyboardInterrupt:
    pass

lcd.lcd_clear()
