#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bluetooth import *
from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time


app = Flask(__name__)

socket = BluetoothSocket( RFCOMM )
socket.connect(("98:D3:91:FD:F6:EA", 1))

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

@app.route("/")
def helloworld():
    return render_template("index.html")
    
@app.route("/<user>")
def user(user):
    return render_template("helloworld.html", name = user)

@app.route("/sensor/<state>")
def sensor(state):
    past_str = ""
    if state == "on":
        data = socket.recv(1024)
        str1 = data.decode()
        
        if "TEMP" in str1:
            size = len(str1)
            return str1[(size - 21):size]
        else:
            return "read_data wait"
    else:
        return "error"

@app.route("/led")
def led():
    state = request.args.get("state", "error");
    type_led = request.args.get("led", "error");
    if state == "on":
        if type_led == "R":
            GPIO.output(21, GPIO.HIGH)
        elif type_led == "G":
            GPIO.output(20, GPIO.HIGH)
        elif type_led == "B":
            GPIO.output(16, GPIO.HIGH)
        elif type_led == "RGB":
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(16, GPIO.HIGH)
        return "ok"
    elif state == "off":
        if type_led == "R":
            GPIO.output(21, GPIO.LOW)
        elif type_led == "G":
            GPIO.output(20, GPIO.LOW)
        elif type_led == "B":
            GPIO.output(16, GPIO.LOW)
        elif type_led == "RGB":
            GPIO.output(21, GPIO.LOW)
            GPIO.output(20, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
        return "ok" 
    elif state == "error":
        return "ont found state"
    else:
        return "error! unknown state"

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
    distance = (int)(duration * 34300) /2
    distance_str = str(distance) + " cm"
    
    if distance <= 10:
        GPIO.output(24, GPIO.HIGH)
    else:
        GPIO.output(24, GPIO.LOW)
        
    return distance_str
    
@app.route("/post", methods=['POST'])
def post():
    value = request.form['test']
    return render_template('helloworld.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
