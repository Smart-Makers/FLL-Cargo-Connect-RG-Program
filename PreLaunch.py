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
#avancer jusqu'au camion
#on_for_degrees(left_speed, right_speed, degrees, brake=True, block=True)
Alpha.on_for_degrees(-60, -60, 1200, brake=True, block=True)
#faire baisser le moyen moteur pour attrapper le camion
m1_m.on_for_degrees(100, 100, brake=True, block=True)
#reculer jusqu'a la base
Alpha.on_for_degrees(60, 60, 1200, brake=True, block=True)
#tourner pour étre completement dans la base
Lm_l.run_forever(speed_sp=150)
Alpha.gyro.wait_until_angle_changed_by(30,True)
Lm_l.stop_actions