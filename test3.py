#!/usr/bin/env micropython
from time import sleep
import time
from ev3dev2 import *
from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor,
                           Motor, MoveSteering, MoveTank, SpeedPercent,
                           follow_for_ms)
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, TouchSensor

# Instantiate the MoveTank object
Alpha = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
Lm_l = Motor(OUTPUT_A)
Lm_r = Motor(OUTPUT_B)
m1_m = Motor(OUTPUT_D)#droite
m2_m = Motor(OUTPUT_C)#gauche
cs = ColorSensor(INPUT_3)
cs.mode = 'COL-REFLECT'

steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
# Initialize the tank's gyro sensor

def LineFollower (time_duration ): 
    time_start = time.time()
    while time.time() < time_start + time_duration:
        if cs.value() > 40 :
            steering_drive.on(20,-20)
        elif cs.value() <= 40 :
            steering_drive.on(-20,-20)
LineFollower(4)

#write your program here
#avancer en utilisant le suiveur de ligne
Alpha.LineFollower(5)
"""#!/usr/bin/env micropython
from time import sleep

from ev3dev2 import *
from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, LargeMotor,
                           Motor, MoveSteering, MoveTank, SpeedPercent,
                           follow_for_ms)
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, TouchSensor

# Instantiate the MoveTank object
Alpha = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
Lm_l = Motor(OUTPUT_A)
Lm_r = Motor(OUTPUT_B)
m1_m = Motor(OUTPUT_D)#droite
m2_m = Motor(OUTPUT_C)#gauche
Alpha.cs = ColorSensor(INPUT_3)
BLACK = 9
WHITE = 93
threshold = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 1.1
Alpha.cs.mode = 'COL-REFLECT'

# Follow the line for 4500ms
def follow_line(self,kp,ki,kd,speed,target_light_intensity=None,follow_left_edge=True,white=60,off_line_count_max=20, sleep_time=0.01,follow_for=follow_for_ms,**kwargs):
    
        PID line follower
        ``kp``, ``ki``, and ``kd`` are the PID constants.
        ``speed`` is the desired speed of the midpoint of the robot
        ``target_light_intensity`` is the reflected light intensity when the color sensor
            is on the edge of the line.  If this is None we assume that the color sensor
            is on the edge of the line and will take a reading to set this variable.
        ``follow_left_edge`` determines if we follow the left or right edge of the line
        ``white`` is the reflected_light_intensity that is used to determine if we have
            lost the line
        ``off_line_count_max`` is how many consecutive times through the loop the
            reflected_light_intensity must be greater than ``white`` before we
            declare the line lost and raise an exception
        ``sleep_time`` is how many seconds we sleep on each pass through
            the loop.  This is to give the robot a chance to react
            to the new motor settings. This should be something small such
            as 0.01 (10ms).
        ``follow_for`` is called to determine if we should keep following the
            line or stop.  This function will be passed ``self`` (the current
            ``MoveTank`` object). Current supported options are:
            - ``follow_for_forever``
            - ``follow_for_ms``
        ``**kwargs`` will be passed to the ``follow_for`` function
        Example:
        .. code:: python
            from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, follow_for_ms
            from ev3dev2.sensor.lego import ColorSensor
            tank = MoveTank(OUTPUT_A, OUTPUT_B)
            tank.cs = ColorSensor()
            try:
                # Follow the line for 4500ms
                tank.follow_line(
                    kp=11.3, ki=0.05, kd=3.2,
                    speed=SpeedPercent(30),
                    follow_for=follow_for_ms,
                    ms=4500
                )
            except LineFollowErrorTooFast:
                tank.stop()
                raise
        

Alpha.follow_line(kp=3.3, ki=0.15, kd=2.2,speed=SpeedPercent(-20),target_light_intensity=None,follow_for=follow_for_ms,ms=4500)
"""