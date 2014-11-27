import sys;
import RPi.GPIO as GPIO
import time


def set_pin(pin,val):
    if(val == 1):
        GPIO.output(pin,GPIO.HIGH);
    else:
        GPIO.output(pin,GPIO.LOW);

def a (pin1,pin2,pin3):
    print "Hello World"
    GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
    GPIO.setup(pin1,GPIO.OUT)
    GPIO.setup(pin2,GPIO.OUT)
    GPIO.setup(pin3,GPIO.OUT)
    
    set_pin(pin1,0);
    set_pin(pin2,0);
    set_pin(pin3,0);
    time.sleep(0.5)
    
    set_pin(pin1,1);
    set_pin(pin2,1);
    set_pin(pin3,1);
    time.sleep(0.5)
    
    for i in (0, 1):
        for j in (0, 1):
            for k in (0,1):
                set_pin(pin1,i);
                set_pin(pin2,j);
                set_pin(pin3,k);
                time.sleep(0.5)
    
    
     #replace pinNum with whatever pin you used, this sets up that pin as an output
    #set LED to flash foreve
def main():
    pin1 = sys.argv[1];
    pin2 = sys.argv[2];
    pin3 = sys.argv[3];
    a(pin1,pin2,pin3);
    
if __name__ == '__main__':
    main();
