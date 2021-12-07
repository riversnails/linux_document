#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import cv2
from bluetooth import *
from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

@app.route("/")
def helloworld():
    return render_template("index.html")
    
@app.route("/camera/on")
def camera():
    #import picamera as camera
    cam=camera.PiCamera()
    cam.resolution = (640,480)
    cam.start_preview()
    #time.sleep(1)
    #print(os.getcwd()+"/picture/test.jpg")
    cam.capture(os.getcwd()+"/static/picture/test.jpg")
    cam.stop_preview()
    cam.close()
    return 'ok'
    
    '''
@app.route("/camera")
def camera():
    state = request.args.get("state", "error");
    type_led = request.args.get("led", "error");
    cam = camera.PiCamera()
    cam.resolution = (640, 480)
    cam.start_preview()
    time.sleep(1)
    cam.capture("/home/pi/Pictures/asdf.jpg")
    cam.stop_preview()
    cam.close()
    return 0
'''

@app.route("/cv2")
def img():
    state = request.args.get("state", "error")
    name = request.args.get("name", "rain.png")
    
    if state == "gray":
        image = cv2.imread(os.getcwd()+"/static/IMG/"+name, cv2.IMREAD_GRAYSCALE)
        print(name)
        cv2.imwrite(os.getcwd()+"/static/picture/gray_copy.jpg", image)
        return "ok"
    elif state == "color":
        image = cv2.imread(os.getcwd()+"/static/IMG/"+name, cv2.IMREAD_COLOR)
        cv2.imwrite(os.getcwd()+"/static/picture/color_copy.jpg", image)
        return "ok"
        
    return "error"

    
@app.route("/post", methods=['POST'])
def post():
    value = request.form['test']
    return render_template('helloworld.html')
    
if __name__ == "__main__":
    import picamera as camera
    app.run(host="0.0.0.0")
