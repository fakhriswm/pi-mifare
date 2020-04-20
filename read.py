#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
myServo = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with $
myServo.start(2.5) # Initialization

reader = SimpleMFRC522()

try:
	while True:
		id, text = reader.read()
		print(id)
		print(text)
		myServo.ChangeDutyCycle(7.5)
		time.sleep(2)
		myServo.ChangeDutyCycle(0.5)
except KeyboardInterrupt :
	GPIO.cleanup()
	myServo.stop()

