#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

@app.route("/")
def helloworld():
    #return "<HTML><BODY bgcolor='green'><H1>HELLO</H1></BODY></HTML>"
    return render_template("index.html")
    
@app.route("/<user>")
def user(user):
    return render_template("helloworld.html", name = user)

@app.route("/led")
def led():
    state = request.args.get("state", "error");
    if state == "on":
        GPIO.output(24, GPIO.HIGH)
        return "ok"
    elif state == "off":
        GPIO.output(24, GPIO.LOW)
        return "ok" 
    elif state == "error":
        return "ont found state"
    else:
        return "error! unknown state"
        
@app.route("/led/<state>")
def led_(state):
    if state == "on":
        GPIO.output(24, GPIO.HIGH)
        return "led on"
    elif state == "off":
        GPIO.output(24, GPIO.LOW)
        return "led off" 
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
    distance = str((int)(duration * 34300) /2) + " cm"
    return distance
    
@app.route("/post", methods=['POST'])
def post():
    value = request.form['test']
    return render_template('helloworld.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
