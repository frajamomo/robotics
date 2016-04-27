import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)
sleep(1)
mylcd.lcd_display_string("Hello World!", 2, 3)
sleep(1)
mylcd.lcd_clear()
sleep(1)

fontdata1 = [
        [ 0b00010,
          0b00100,
          0b01000,
          0b10000,
          0b01000,
          0b00100,
          0b00010,
          0b00000 ],
]

mylcd.lcd_load_custom_chars(fontdata1)
mylcd.lcd_write(0x80)
mylcd.lcd_write_char(0)
