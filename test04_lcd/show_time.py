import lcddriver
import datetime
import time

INTERVAL = 1

lcd = lcddriver.lcd()

def getTimeList():
    """
    Fetches a list of time units the cpu has spent in various modes
    Detailed explanation at http://www.linuxhowtos.org/System/procstat.htm
    """
    cpuStats = file("/proc/stat", "r").readline()
    columns = cpuStats.replace("cpu", "").split(" ")
    return map(int, filter(None, columns))

def deltaTime(interval):
    """
    Returns the difference of the cpu statistics returned by getTimeList
    that occurred in the given time delta
    """
    timeList1 = getTimeList()
    time.sleep(interval)
    timeList2 = getTimeList()
    return [(t2-t1) for t1, t2 in zip(timeList1, timeList2)]

def getCpuLoad():
    """
    Returns the cpu load as a value from the interval [0.0, 1.0]
    """
    dt = list(deltaTime(INTERVAL))
    idle_time = float(dt[3])
    total_time = sum(dt)
    load = 1-(idle_time/total_time)
    return load

try:
    while True:
        ahora_dia  = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        ahora_hora = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
        ahora_hora = ahora_hora + "    %.2f%%" % (getCpuLoad()*100.0)

        lcd.lcd_display_string(ahora_dia, 1)
        lcd.lcd_display_string(ahora_hora, 2)
        time.sleep(1)
except KeyboardInterrupt:
    pass

lcd.lcd_clear()
