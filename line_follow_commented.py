#!/usr/bin/env pybricks-micropython
'''Possible Improvments
There is some room for improvents
Few of them include:
 Make a sensor calibrator
 Find a way to put more speed on when error is low
'''
from pybricks.ev3devices import Motor,ColorSensor
from pybricks.parameters import Port
# Initialize the motors
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
# Initialize the sensors 
color1=ColorSensor(Port.S1)
color2=ColorSensor(Port.S2)
color3=ColorSensor(Port.S3)
color4=ColorSensor(Port.S4)
# right_motor.dc(a) (skip)
# left_motor.dc(a) (skip)
# Initialize the sensors
l_err=0
while True:
    # Calculate Front sensor error
    err1 =  (color2.reflection()-color3.reflection())
    # Calculate Back sensor error multiply by back kp(4) and add it to Front multiplied by front kp(1.35) 
    error = err1*1.35 + (color4.reflection()-color1.reflection())*4
    # Calculate Derivative
    der=(error-l_err)*3
    # Add it to speed (speed = 80)
    left_motor.dc(80+(der+error))
    # Multiply with -1 because of reverse motors
    right_motor.dc(-(80-(der+error)))
    #l_err for the kd
    l_err = error