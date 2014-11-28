import sys
import os
import RPi.GPIO as GPIO
import time

def set_pin(pin,val):
    if(val == 1):
        GPIO.output(pin,GPIO.HIGH);
    else:
        GPIO.output(pin,GPIO.LOW);

def start (pin1,pin2,pin3, pin_in):
    GPIO.setup(pin_in,GPIO.IN)
    pin_prev_state = 0;
    while True:
        if(GPIO.input(pin_in)):
            if(pin_prev_state == 0):
                os.system("python led.py "+str(pin1)+" "+str(pin2)+" "+str(pin3))
                pin_prev_state = 1
        else:
            pin_prev_state = 0    
        
def main():
    pin1 = sys.argv[1];
    pin2 = sys.argv[2];
    pin3 = sys.argv[3];
    pin4 = sys.argv[4];
    
    start(int(pin1),int(pin2),int(pin3), int(pin4));
    
if __name__ == '__main__':
    main();
