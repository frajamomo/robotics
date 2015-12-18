#!/usr/bin/python

from select import select
from evdev import InputDevice, categorize, ecodes, KeyEvent

gamepad = InputDevice('/dev/input/event1')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            print keyevent.keycode
    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
    elif event.type == ecodes.EV_SYN:
        synevent = categorize(event)
        print synevent
