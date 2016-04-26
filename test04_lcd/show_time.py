import lcddriver
import datetime
from time import sleep, strftime
#from datetime import datetime

#from subprocess import *

#def run_cmd(cmd):
#    p = Popen(cmd, shell=True, stdout=PIPE)
#    output = p.communicate()[0]
#    return output

lcd = lcddriver.lcd()

#cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

#lcd.lcd_clear()
try:
    while True:
#        ipaddr = run_cmd(cmd)
#        lcd.lcd_display_string(datetime.now().strftime('%b %d %H:%M:%S'), 1)
#        lcd.lcd_display_string('IP: %s' % ( ipaddr ), 2)
#        print "Line 1: %s" % ( datetime.now().strftime('%b %d %H:%M:%S') )
#        print "Line 2: %s" % ( "IP: %s" % ( ipaddr ) )
        ahora_dia  = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        ahora_hora = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
        lcd.lcd_display_string(ahora_dia, 1)
        lcd.lcd_display_string(ahora_hora, 2)
        sleep(1)
except KeyboardInterrupt:
    pass

lcd.lcd_clear()
