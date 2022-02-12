#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor,Motor, OUTPUT_A, OUTPUT_B,OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.motor import OUTPUT_A, OUTPUT_B,MoveSteering, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
# Instantiate the MoveTank object
Alpha = MoveTank(OUTPUT_A, OUTPUT_B)
Lm_l = Motor(OUTPUT_A)
Lm_r = Motor(OUTPUT_B)
m1_m = Motor(OUTPUT_D)#droite
m2_m = Motor(OUTPUT_C)#gauche
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
# Initialize the tank's gyro sensor
Alpha.gyro = GyroSensor()

# Calibrate the gyro to eliminate drift, and to initialize the current angle as 0
Alpha.gyro.calibrate()
#write your program here
#avancer en tournant un peu jusqu'au pont
Alpha.on_for_degrees(-60, -55, 2000, brake=True, block=True)
#lever le moyen moteur
m1_m.on_for_degrees(100, 100, brake=True, block=True)
#reculer jusqu'a la base
Alpha.on_for_degrees(60, 60, 2500, brake=True, block=True)