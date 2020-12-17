import RPi.GPIO as GPIO
import time
from gpiozero import DigitalInputDevice

#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print(str(GPIO.input(channel)))
        print("water detected")
    else:
        print(str(GPIO.input(channel)))  
        print("no water detected")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
