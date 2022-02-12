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
m1_m = Motor(OUTPUT_D)#gauche   
m2_m = Motor(OUTPUT_C)#droite                                          # NEW L5 PROGRAM HERE
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)
# Initialize the tank's gyro sensor
Alpha.gyro = GyroSensor()

# Calibrate the gyro to eliminate drift, and to initialize the current angle as 0
Alpha.gyro.calibrate()
# avancer jusqu'a la plateforme
steering_drive.on_for_degrees(0,-60,1950,brake=True,block=True)
# tourner à droite
Lm_l.run_forever(speed_sp=-80)
Alpha.gyro.wait_until_angle_changed_by(50,True)
Lm_l.stop_actions
# avancer un peu
steering_drive.on_for_degrees(0,-50,460,brake=True,block=True)
# tourner à gauche pour s'aligner avec la plateforme
Lm_r.run_forever(speed_sp=-100)
Alpha.gyro.wait_until_angle_changed_by(-90,True)
Lm_r.stop_actions
# avancer un peu
steering_drive.on_for_degrees(0,-50,100,brake=True,block=True)
# baisser le myen moteur de droite pour poser les conteneurs sur la plateforme
m2_m.on_for_degrees(-100, 2000, brake=True, block=True)