from evdev import InputDevice, list_devices

gamepad = InputDevice('/dev/input/event1')
print (gamepad)


print "Listing accessible events devices"

devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    print(dev.fn, dev.name, dev.phys)

print "\nDevice capabilities:"
print (gamepad.capabilities())
print "--------------------------------"
print "Device capabilities verbose:"
print gamepad.capabilities(verbose=True)
print "--------------------------------"
