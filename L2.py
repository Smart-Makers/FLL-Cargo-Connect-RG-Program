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
#avancer jusqu'a l'helicopter
steering_drive.on_for_degrees(0,-60,1525,brake=True, block=True)
#tourner un peu à droite pour s'aligné avec la mission
Lm_l.run_forever(speed_sp=-100)
Alpha.gyro.wait_until_angle_changed_by(15,True)
Lm_l.stop_actions
#avancer un peu
steering_drive.on_for_degrees(0,-10,5,brake=True,block=True)
#baisser le moyen moteur gauche
m1_m.on_for_degrees(-80, 400, brake=True, block=True)
#lever le moyen moteur gauche un peu
m1_m.on_for_degrees(30, 50, brake=True, block=True)
# reculer un peu
steering_drive.on_for_degrees(0,50,30,brake=True,block=True)
#tourner à droite pour deposer le contenaire vert
Lm_l.run_forever(speed_sp=-80)
Alpha.gyro.wait_until_angle_changed_by(15,True)
Lm_l.stop_actions
# avancer un peu
steering_drive.on_for_degrees(0,-100,100,brake=True,block=True)
# baisser le moyen moteur droit
m2_m.on_for_degrees(-60, 800, brake=True, block=True)
# reculer pour rentrer à la base
steering_drive.on_for_degrees(0,100,1600,brake=True,block=True)



