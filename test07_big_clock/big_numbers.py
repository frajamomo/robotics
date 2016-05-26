import I2C_LCD_driver
import time


fontdata1 = [
        # char(0)
        [ 0b00011,   #      xx
          0b00111,   #     xxx
          0b01111,   #    xxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111 ], #   xxxxx

        # char(1)
        [ 0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b00000,   #
          0b00000,   #
          0b00000,   #
          0b00000,   #
          0b00000 ], #

        # char(2)
        [ 0b00000,   #
          0b00000,   #
          0b00000,   #
          0b00000,   #
          0b00000,   #
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111 ], #   xxxxx

        # char(3)
        [ 0b00000,   #
          0b00000,   #
          0b00000,   #
          0b00000,   #
          0b00000,   #
          0b00000,   #
          0b11111,   #   xxxxx
          0b11111 ], #   xxxxx

        # char(4)
        [ 0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b01111,   #    xxxx
          0b00111 ], #     xxx

        # char(5)
        [ 0b11100,   #   xxx
          0b11110,   #   xxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111 ], #   xxxxx

        # char(6)
        [ 0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11110,   #   xxxx
          0b11100 ], #   xxx

        # char(7)
        [ 0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111 ], #   xxxxx

        # char(8)
        [ 0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b00000,   #
          0b00000,   #
          0b00000,   #
          0b11111,   #   xxxxx
          0b11111 ], #   xxxxx

        # char(9)
        [ 0b00111,   #      xx
          0b01111,   #     xxx
          0b11111,   #    xxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111,   #   xxxxx
          0b11111 ], #   xxxxx

        # char(10) - Upper-left character
        [ 0b11111,
          0b11111,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000 ],

]


def print_zero(lcd):
    lcd.lcd_write(0x80)
    lcd.lcd_write_char(9)
    lcd.lcd_write_char(10)
    lcd.lcd_write_char(5)

    lcd.lcd_write(0xC0)
    lcd.lcd_write_char(4)
    lcd.lcd_write_char(3)
    lcd.lcd_write_char(6)
    return

def print_one(lcd):
    lcd.lcd_write(0x80)
    lcd.lcd_write_char(10)
    lcd.lcd_write_char(7)
    lcd.lcd_write_char(5)

    lcd.lcd_write(0xC0)
    lcd.lcd_write_char(4)
    lcd.lcd_write_char(3)
    lcd.lcd_write_char(6)
    return

def main():
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_clear()
    mylcd.lcd_load_custom_chars(fontdata1)

    print_zero(mylcd)
    time.sleep(5)
    mylcd.lcd_clear()
    time.sleep(1)

    print_one(mylcd)

if __name__ == "__main__":
    main()
