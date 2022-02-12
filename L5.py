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
# write your program here
#avancer pour passer entre le camions et l'avion
steering_drive.on_for_degrees(0,-60,1950,brake=True,block=True)
# tourner à droite
Lm_l.run_forever(speed_sp=-80)
Alpha.gyro.wait_until_angle_changed_by(55,True)
Lm_l.stop_actions
#wait
steering_drive.wait_until_not_moving()
Alpha.gyro.reset()
# avancer un peu
steering_drive.on_for_degrees(0,-50,200,brake=True,block=True)
# tourner à gauche
Lm_l.run_forever(speed_sp=-90)
Alpha.gyro.wait_until_angle_changed_by(90,True)
Lm_l.stop_actions
# avancer un peu
steering_drive.on_for_degrees(0,-60,200,brake=True,block=True)
# lacher les contenaire sur la plateforme
m2_m.on_for_degrees(-40, 1500, brake=True, block=True)

