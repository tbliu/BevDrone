import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
# set pin 7 to be pin that connects to button
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
prev_input = 1

while True:
    curr_input = GPIO.input(7)
    if ((not prev_input) and curr_input):
        # run servo motor script
        # os.system("python /home/pi/bevdrone/claw/servo_grab.py")
        print("Button pressed")
    else:
        # os.system("python /home/pi/bevdrone/claw/servo_release.py")
    prev_input = curr_input
    time.sleep(0.05)

