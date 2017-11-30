import RPi.GPIO as GPIO
import time
import subprocess


GPIO.setmode(GPIO.BOARD)
# set pin 7 to be pin that connects to button
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
prev_input = 1
closed = False
while True:
    curr_input = GPIO.input(7)
    if ((not prev_input) and curr_input and not closed):
        # run servo motor script
        subprocess.call(["python", "servo_grab.py"])
        closed = True
        print("Close servo")
    elif ((not prev_input) and curr_input and closed):
        subprocess.call(["python", "servo_release.py"])
        closed = False
        print("Open servo")
    prev_input = curr_input
    time.sleep(0.05)

