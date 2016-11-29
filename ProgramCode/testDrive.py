from time import sleep
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
sleep(1)
isTrig = False

def trig():
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)


while True:
        print "LED on"
        GPIO.output(18,GPIO.HIGH)

        if isTrig == True:
            trig();
        result = GPIO.input(6)
        if result == 1:
            print("VIbrated")
            isTrig =True
 	    sleep(1)            

