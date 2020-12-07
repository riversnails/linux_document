'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gpio.py
#  
#  Copyright 2020  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import RPi.GPIO as GPIO
import time

LED_PIN = 21
PUSH_PIN = 17
PUSH_PIN2 = 27


def main(args):
    in1 = 20
    in2 = 16
    toggle = 0
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(PUSH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PUSH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    
    
    try:
        while True:
            if GPIO.input(PUSH_PIN) == GPIO.LOW:
                print("Push DOWN")
            else:
                print("Push UP")
                if toggle == 0:
                    toggle = 1
                    GPIO.output(in1, GPIO.HIGH)
                    GPIO.output(in2, GPIO.LOW)
                elif toggle == 1:
                    toggle = 0
                    GPIO.output(in1, GPIO.LOW)
                    GPIO.output(in2, GPIO.HIGH)
                
            if GPIO.input(PUSH_PIN2) == GPIO.LOW:
                print(" Push1 DOWN")
            else:
                print(" Push1 UP")
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.LOW)
                
            print(toggle)
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()    
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))'''


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gpio.py
#  
#  Copyright 2020  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import RPi.GPIO as GPIO
import time

LED_PIN = 21
PUSH_PIN = 17
PUSH_PIN2 = 27


def main(args):
    in1 = 20
    in2 = 16
    toggle = 0
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(PUSH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PUSH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    
    ledPWM = GPIO.PWM(in1, 50)
    ledPWM.start(0)
    
    try:
        while True:
            if GPIO.input(PUSH_PIN) == GPIO.LOW:
                print("Push DOWN")
            else:
                print("Push UP")
                ledPWM.start(0)
                if toggle == 0:
                    toggle = 1
                    ledPWM.ChangeDutyCycle(16)
                elif toggle == 1:
                    toggle = 2
                    ledPWM.ChangeDutyCycle(32)
                elif toggle == 2:
                    toggle = 0
                    ledPWM.ChangeDutyCycle(50)
                
            if GPIO.input(PUSH_PIN2) == GPIO.LOW:
                print(" Push1 DOWN")
            else:
                print(" Push1 UP")
                ledPWM.ChangeDutyCycle(1)
            print(toggle)
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()    
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
