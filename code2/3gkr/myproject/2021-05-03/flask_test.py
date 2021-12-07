#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

@app.route("/")
def helloworld():
    return "Hello World"
    
@app.route("/led/on")
def led_on():
    GPIO.output(24, GPIO.HIGH)
    return "led on"

@app.route("/led/off")
def led_off():
    GPIO.output(24, GPIO.LOW)
    return "led off"    

@app.route("/ultra/read")
def jodo_read():
    start_time = 0
    end_time = 0
    
    GPIO.output(25, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(25, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(25, GPIO.LOW)
    
    while GPIO.input(12) == GPIO.LOW:
        start_time = time.time()
        
    while GPIO.input(12) == GPIO.HIGH:
        end_time = time.time()
        
    duration = (float)(end_time - start_time)
    distance = str((duration * 34300) /2) + " cm"
    return distance
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
