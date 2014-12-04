#!/usr/bin/env python

import pygame
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Initialise the pygame library
pygame.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()

print 'Initialized Joystick : %s' % j.get_name()

# Setup the various GPIO values, using the BCM numbers for now
MotorA0 = 16
MotorA1 = 18
MotorA00 = 6
MotorA11 = 13


MotorB0 = 23
MotorB1 = 21
MotorB00 = 11
MotorB11 = 9

A0 = False
A1 = False
B0 = False
B1 = False
A00 = False
A11 = False
B00 = False
B11 = False


GPIO.setup(MotorA0,GPIO.OUT)
GPIO.setup(MotorA1,GPIO.OUT)
GPIO.setup(MotorA00,GPIO.OUT)
GPIO.setup(MotorA11,GPIO.OUT)

GPIO.setup(MotorB0,GPIO.OUT)
GPIO.setup(MotorB1,GPIO.OUT)
GPIO.setup(MotorB00,GPIO.OUT)
GPIO.setup(MotorB11,GPIO.OUT)

# Set all the Motors to 'off'
GPIO.output(MotorA0, A0)
GPIO.output(MotorA1, A1)
GPIO.output(MotorB0, B0)
GPIO.output(MotorB1, B1)
GPIO.output(MotorA00, A00)
GPIO.output(MotorA11, A11)
GPIO.output(MotorB00, B00)
GPIO.output(MotorB11, B11)


# Only start the motors when the inputs go above the following threshold
threshold = 0.60


LeftTrack = 0
RightTrack = 0
LeftTurn = 0
RightTurn = 0

# Configure the motors to match the current settings.

def setmotors():
        GPIO.output(MotorA0, A0)
        GPIO.output(MotorA1, A1)
        GPIO.output(MotorB0, B0)
        GPIO.output(MotorB1, B1)
        GPIO.output(MotorA00, A00)
        GPIO.output(MotorA11, A11)
        GPIO.output(MotorB00, B00)
        GPIO.output(MotorB11, B11)
# Try and run the main code, and in case of failure we can stop the motors
try:
    # Turn on the motors# This is the main loop
    while True:

        # Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
          UpdateMotors = 0

          # Check if one of the joysticks has moved
          if event.type == pygame.JOYAXISMOTION:
            if event.axis == 1:
              LeftTrack = event.value
              UpdateMotors = 1
            elif event.axis == 2:
              LeftTurn = event.value
              UpdateMotors = 1
            elif event.axis == 3:
              RightTrack = event.value
              UpdateMotors = 1
            elif event.axis == 4:
              RightTurn = event.value
              UpdateMotors = 1

            # Check if we need to update what the motors are doing
            if UpdateMotors:

              # Check how to configure the left motor

              # Move forwards
              if (RightTrack > threshold):
                  A0 = False
                  A1 = True
              # Move backwards
              elif (RightTrack < -threshold):
                  A0 = True
                  A1 = False
              # Stopping
              else:
                  A0 = False
                  A1 = False


              # And do the same for the right motor
              if (LeftTrack > threshold):
                  B0 = False
                  B1 = True
              # Move backwards
              elif (LeftTrack < -threshold):
                  B0 = True
                  B1 = False
              # Otherwise stop
              else:
                  B0 = False
                  B1 = False

              # Move LEft 
              if (LeftTurn > threshold):
                  B00 = False
                  B11 = True
              # Move backwards
              elif (LeftTurn < -threshold):
                  B00 = True
                  B11 = False
              # Stopping
              else:
                  B00 = False
                  B11 = False
                  
                                
                            # Move forwards
              if (RightTurn > threshold):
                  A00 = False
                  A11 = True
              # Move backwards
              elif (RightTurn < -threshold):
                  A00 = True
                  A11 = False
              # Stopping
              else:
                  A00 = False
                  A11 = False                   # Now we've worked out what is going on we can tell the
              # motors what they need to do
              setmotors()


except KeyboardInterrupt:
    # Turn off the motors
    j.quit()#!/usr/bin/env python

GPIO.cleanup()