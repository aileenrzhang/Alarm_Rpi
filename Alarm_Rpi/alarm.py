#!/usr/bin/env python

import schedule
import subprocess
import time
from gpiozero import Button
import sys
import RPi.GPIO as GPIO
import json

json_alarmtime = json.dum

minutes_before_alarm = 1
seconds_before_alarm = minutes_before_alarm * 60

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

button = Button(17)


def job():
    global seconds_before_alarm
    time_between_leds = seconds_before_alarm / 7
    
    GPIO.output(5,GPIO.HIGH)
    time.sleep(time_between_leds)
    GPIO.output(6, GPIO.HIGH)
    time.sleep(time_between_leds)
    GPIO.output(16,GPIO.HIGH)
    time.sleep(time_between_leds)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(time_between_leds)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(time_between_leds)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(time_between_leds)
    GPIO.output(25,GPIO.HIGH)
    time.sleep(time_between_leds)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(time_between_leds)
    
    subprocess.call(['aplay /home/pi/Alarm_Rpi/alarm_quiet_for_testing.wav'], shell=True)
    
alarm_time = '19:53'
str_times = alarm_time.split(':')

times = [0,0]

times[0] = int(str_times[0])
times[1] = int(str_times[1])

if (times[1] > minutes_before_alarm):
    times[1] = times[1] - minutes_before_alarm
else:
    times[1] = 60 - (minutes_before_alarm - times[1])
    if times[0] == 0:
        times[0] = 23
    else:
        times[0] = times[0] - 1
        
alarm_time = str(times[0]) + ':' + str(times[1])

schedule.every().day.at(alarm_time).do(job)


while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except button.wait_for_press():
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        break