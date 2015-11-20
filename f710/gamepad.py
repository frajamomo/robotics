#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event1')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.keycode[0] == 'BTN_A':
                print "Back"
            elif keyevent.keycode[0] == 'BTN_WEST':
                print "Forward"
            elif keyevent.keycode[0] == 'BTN_B':
                print "Right"
            elif keyevent.keycode[0] == 'BTN_NORTH':
                print "Left"
            elif keyevent.keycode == 'BTN_THUMBL':
                print "Left thumb button"
            elif keyevent.keycode == 'BTN_THUMBR':
                print "Right thumb button - EXITING"
                exit()
            elif keyevent.keycode == 'BTN_START':
                print "Start button"
            elif keyevent.keycode == 'BTN_SELECT':
                print "Select button"
            elif keyevent.keycode == 'BTN_MODE':
                print "mode button"
    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
#    elif event.type == ecodes.EV_SYN:
#        synevent = categorize(event)
#        print "----->", synevent
