#!/usr/bin/python
from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event1')
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
    else:
        print "Not a button"
