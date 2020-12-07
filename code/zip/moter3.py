import RPi.GPIO as g
import time

PUSH_PIN1 = 17
PUSH_PIN2 = 16
FAN_PIN1 = 21
FAN_PIN2 = 20

toggle1 = 0
toggle2 = 0
toggle = 0

def main(args):
    g.setmode(g.BCM)
    
    g.setup(PUSH_PIN1, g.IN, pull_up_down = g.PUD_UP)
    g.setup(PUSH_PIN2, g.IN, pull_up_down = g.PUD_UP)
    
    g.setup(FAN_PIN1, g.OUT)
    g.setup(FAN_PIN2, g.OUT)
    
    
    try:
        global toggle1
        global toggle2
        global toggle
        
        fanPWM = g.PWM(FAN_PIN1, 100)
        fanPWM.start(0)
        fanPWM.ChangeDutyCycle(0)
        
        while True:
            if g.input(PUSH_PIN1) == g.LOW:
                if toggle1 == 0:
                    if toggle == 0:
                        fanPWM.ChangeDutyCycle(30)
                        g.output(FAN_PIN2, g.LOW)
                        toggle = 1
                    elif toggle == 1:
                        fanPWM.ChangeDutyCycle(60)
                        g.output(FAN_PIN2, g.LOW)
                        toggle = 2
                    elif toggle == 2:
                        fanPWM.ChangeDutyCycle(100)
                        g.output(FAN_PIN2, g.LOW)
                        toggle = 0
                    print("push1 DOWN")
                    toggle1 = 1
            else:
                if toggle1 == 1:
                    toggle1 = 0
                    print("push1 UP")
            if g.input(PUSH_PIN2) == g.LOW:
                if toggle2 == 0:
                    fanPWM.ChangeDutyCycle(0)
                    g.output(FAN_PIN2, g.LOW)
                    print("push2 DOWN")
                    toggle2 = 1
                    toggle = 0
            else:
                if toggle2 == 1:
                    toggle2 = 0
                    print("push2 UP")
            
            time.sleep(0.1)
        
    except KeyboardInterrupt:
        g.cleanup()
    
if __name__ == '__main__':
    import sys
    
    sys.exit(main(sys.argv))