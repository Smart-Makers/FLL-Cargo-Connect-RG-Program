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
steering_drive.on_for_degrees(0,-60,2600,brake=True,block=True)

# baisser le myen moteur de droite pour poser les conteneurs sur la plateforme
m2_m.on_for_degrees(-100, 2000, brake=True, block=True)

#reculer
steering_drive.on_for_degrees(0,60,500,brake=True,block=True)

#tourner à droite
Lm_l.run_forever(speed_sp=-80)
Alpha.gyro.wait_until_angle_changed_by(35,True)
Lm_l.stop_actions

#avancer 
steering_drive.on_for_degrees(0,-60,300,brake=True,block=True)
# baisser le trait
m1_m.on_for_degrees(-80, 200, brake=True, block=True)
# zide nichane 7ta te7errek dik mini tower
steering_drive.on_for_degrees(0,-60,600,brake=True,block=True)
# lever le trait
m1_m.on_for_degrees(80, 400, brake=True, block=True)
steering_drive.on_for_degrees(0,60,400,brake=True,block=True)

Lm_l.run_forever(speed_sp=-150)
Alpha.gyro.wait_until_angle_changed_by(45,True)
Lm_l.stop_actions
steering_drive.on_for_degrees(0,60,700,brake=True,block=True)
Lm_l.run_forever(speed_sp=150)
Alpha.gyro.wait_until_angle_changed_by(-45,True)
Lm_l.stop_actions
steering_drive.on_for_degrees(0,60,200,brake=True,block=True)
