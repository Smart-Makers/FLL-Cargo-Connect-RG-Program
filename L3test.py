#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor,Motor, OUTPUT_A, OUTPUT_B,OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.led import Leds
from ev3dev2.motor import OUTPUT_A, OUTPUT_B,MoveSteering, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, TouchSensor
import time
from time import sleep
# Instantiate the MoveTank object
Alpha = MoveTank(OUTPUT_A, OUTPUT_B)
Lm_l = Motor(OUTPUT_A)
Lm_r = Motor(OUTPUT_B)
m1_m = Motor(OUTPUT_D)#droite
m2_m = Motor(OUTPUT_C)#gauche
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
cs = ColorSensor(INPUT_3)
cs.mode = 'COL-REFLECT'
# Initialize the tank's gyro sensor
Alpha.gyro = GyroSensor()

# Calibrate the gyro to eliminate drift, and to initialize the current angle as 0
Alpha.gyro.calibrate()
#write your program here
steering_drive.wait_until_not_moving()
Alpha.gyro.reset()
#avancer jusqu'au pont
Alpha.on_for_degrees(-100, -100, 1950, brake=True, block=True)
#tourner un peu à gauche
Lm_l.run_forever(speed_sp=-90)
Alpha.gyro.wait_until_angle_changed_by(35,True)
Lm_l.stop_actions
#avancer jusqu'au logo Cargo Connect
steering_drive.on_for_degrees(0,-30,500,brake=True, block=True)
#tourner a droite
Lm_l.run_forever(speed_sp=-100)
Alpha.gyro.wait_until_angle_changed_by(50,True)
Lm_l.stop_actions
#avancer un peu
steering_drive.on_for_degrees(0,-30,10,brake=True, block=True)
#faire tomber le PI
m2_m.on_for_degrees(30, 900, brake=True, block=True)
#remonter le moyen moteur
m2_m.on_for_degrees(-100, 900, brake=True, block=True)
#reculer un peu
steering_drive.on_for_degrees(0,60,175,brake=True, block=True)
#tourner à gauche
Lm_r.run_forever(speed_sp=-100)
Alpha.gyro.wait_until_angle_changed_by(-43,True)
Lm_r.stop_actions
#avancer jusqu'au train
steering_drive.on_for_degrees(0,-60,670,brake=True, block=True)
#tourner à gauche
Lm_r.run_forever(speed_sp=-150)
Alpha.gyro.wait_until_angle_changed_by(-50,True)
Lm_r.stop_actions
#avancer un peu
steering_drive.on_for_degrees(0,-60,150,brake=True, block=True)
#reculer un peu
steering_drive.on_for_degrees(0,60,120,brake=True, block=True)
#tourner à gauche
Lm_r.run_forever(speed_sp=-150)
Alpha.gyro.wait_until_angle_changed_by(-20,True)
Lm_r.stop_actions
#avancer un peu
steering_drive.on_for_degrees(0,-60,10,brake=True, block=True)
#baisser le moyen moteur pour faire tomber le contenaire 
m1_m.on_for_degrees(100, 1100, brake=True, block=True)
#faire monter le moyen moteur
m1_m.on_for_degrees(-100, 1100, brake=True, block=True)
