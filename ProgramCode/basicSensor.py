from time import sleep
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
sleep(1)

while True:
        result = GPIO.input(6)
        if result == 1:
            print("VIbrated")
 	    sleep(1)            

    
