
import RPi.GPIO as GPIO
import time


count=0
def main (count):
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
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.1)
    #Frontbumper
    GPIO.output(4,GPIO.HIGH)
    # Roof right
    GPIO.output(26,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(4,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    #Roof left
    GPIO.output(13,GPIO.HIGH)
    time.sleep(0.3)
    #GPIO.output(4,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(26,GPIO.HIGH)
    ## front 
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.HIGH)
    time.sleep(0.1)
    # 4
def clean (count):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)
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
    print "Cleaned after ",count, " runs"
def lightblink (count):
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
    print "Shutting off car after",count, " runs, blink blink."
    GPIO.output(5,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.2)
clean(count)
lightblink(count)
while count < 30:
    print "Starting run", count, "..."
    count += 1
    main(count)
lightblink(count)
clean(count)
