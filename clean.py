import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.output(26,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(17,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(5,GPIO.LOW)
GPIO.cleanup() # cleanup all GPIO 
