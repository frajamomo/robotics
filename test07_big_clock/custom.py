import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

#mylcd.lcd_display_string("Hello World!", 1)
#sleep(1)
#mylcd.lcd_display_string("Hello World!", 2, 3)
#sleep(1)
#mylcd.lcd_clear()
#sleep(1)
#
#fontdata1 = [
#        [ 0b00010,
#          0b00100,
#          0b01000,
#          0b10000,
#          0b01000,
#          0b00100,
#          0b00010,
#          0b00000 ],
#]
#
#mylcd.lcd_load_custom_chars(fontdata1)
#mylcd.lcd_write(0x80)
#mylcd.lcd_write_char(0)
#sleep(1)
#mylcd.lcd_clear()

try:
    while True:
        my_big_clock.display_current_time()
        sleep(1)
except KeyboardInterrupt:
    pass
my_big_clock.clear()

#str_pad = " " * 16
#my_long_string = "This is a string that needs to scroll"
#my_long_string = str_pad + my_long_string
#
#for i in range (0, len(my_long_string)):
#    lcd_text = my_long_string[i:(i+16)]
#    mylcd.lcd_display_string(lcd_text,1)
#    sleep(0.4)
#    mylcd.lcd_display_string(str_pad,1)
#
#sleep(1)

#import socket
#import fcntl
#import struct
#
#
#def get_ip_address(ifname):
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    return socket.inet_ntoa(fcntl.ioctl(
#        s.fileno(),
#        0x8915,
#        struct.pack('256s', ifname[:15])
#    )[20:24])
#
#mylcd.lcd_display_string("IP Address:", 1)
#
#mylcd.lcd_display_string(get_ip_address('eth0'), 2)
#sleep(10)

mylcd.lcd_clear()

fontdata1 = [
        # char(0) - Upper-left character
        [ 0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b11111,
          0b11111 ],

        # char(1) - Upper-middle character
        [ 0b00000,
          0b00000,
          0b00100,
          0b00110,
          0b00111,
          0b00111,
          0b11111,
          0b11111 ],

        # char(2) - Upper-right character
        [ 0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b10000,
          0b11000 ],

        # char(3) - Lower-left character
        [ 0b11111,
          0b11111,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000 ],

        # char(4) - Lower-middle character
        [ 0b11111,
          0b11111,
          0b00111,
          0b00111,
          0b00110,
          0b00100,
          0b00000,
          0b00000 ],

        # char(5) - Lower-right character
        [ 0b11000,
          0b10000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000 ],

# char(6) - Personajillo
        [   0b00100,
            0b01010,
            0b00100,
            0b11111,
            0b00100,
            0b00100,
            0b01010,
            0b10001 ],
]

mylcd.lcd_load_custom_chars(fontdata1)

mylcd.lcd_write(0x80)
mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)
mylcd.lcd_write_char(6)

mylcd.lcd_write(0xC0)
mylcd.lcd_write_char(3)
mylcd.lcd_write_char(4)
mylcd.lcd_write_char(5)
mylcd.lcd_write_char(6)
