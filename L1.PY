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

#write your programm here
#avancer jusqu'au pont
steering_drive.on_for_degrees(0,-50,1750,brake=True, block=True)
#wait
steering_drive.wait_until_not_moving()
Alpha.gyro.reset()
#gyro functions
Lm_l.run_forever(speed_sp=-80)
Alpha.gyro.wait_until_angle_changed_by(55,True)
Lm_l.stop_actions
#avancer jusqu'au train
steering_drive.on_for_degrees(0,-50,1390,brake=True, block=True)
#gyro functions
Lm_l.run_forever(speed_sp=-80)
Alpha.gyro.wait_until_angle_changed_by(40,True)
Lm_l.stop_actions
#avancer un peu
steering_drive.on_for_degrees(0,-80,250,brake=True, block=True)
#gyro functions
Lm_l.run_forever(speed_sp=-120)
Alpha.gyro.wait_until_angle_changed_by(55,True)
Lm_l.stop_actions
#avancer jusqu'a la mission
steering_drive.on_for_degrees(0,-30,400,brake=True, block=True)
#baisser le moyen moteur pour faire descendre le colis
m2_m.on_for_degrees(70, 2000, brake=True, block=True)
#monter le moyen moteur pour prendre les contenaire
m2_m.on_for_degrees(-100,2000 , brake=True, block=True)
m1_m.on_for_degrees(-100, 120, brake=True, block=True)
#reculer un peu
steering_drive.on_for_degrees(0,60,400,brake=True, block=True)
#tourner a droite
Lm_l.run_forever(speed_sp=-120)
Alpha.gyro.wait_until_angle_changed_by(40,True)
Lm_l.stop_actions
#avancer
steering_drive.on_for_degrees(0,-100,800,brake=True, block=True)
#tourner a droite
Lm_l.run_forever(speed_sp=-150)
Alpha.gyro.wait_until_angle_changed_by(55,True)
Lm_l.stop_actions
#avancer pour rentrer a la base
steering_drive.on_for_degrees(0,-100,7000,brake=True, block=True)
