#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice('/dev/input/event1')

for event in gamepad.read_loop():
    keyevent = categorize(event)
    print keyevent, "||", event

