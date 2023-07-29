import cwiid
from time import sleep
from gpiozero import Robot
robot = Robot(left=(14,15), right=(23,18))
print("Press 1 + 2 to set the wiimote into pairing mode")
sleep(3)
try:
    wii=cwiid.Wiimote()
    wii.rpt_mode = cwiid.RPT_BTN
except NameError and RuntimeError:
    print("I couldn't see a Wiimote")
    exit()
while True:
    buttons = wii.state['buttons']
    if buttons & cwiid.BTN_UP:
        robot.forward()
    elif buttons & cwiid.BTN_DOWN:
        robot.backward()
    elif buttons & cwiid.BTN_A:
        robot.stop()
    elif buttons == 12:
        print("You pressed the A & B button together!")
    print(buttons)
    sleep(0.1)
