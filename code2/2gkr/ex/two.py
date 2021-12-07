from sense_hat import SenseHat
import time

O = [0, 0, 0]
X = [255, 255, 255] 

question_mark0 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, X, O, O, X, O, O,
O, X, O, X, X, O, X, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, X, X, O, O, O
]

question_mark1 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, X, O, O, X, O, O,
O, X, O, X, X, O, X, O,
O, O, X, O, O, X, O, O,
X, O, O, O, O, O, O, X,
O, X, X, X, X, X, X, O,
O, O, X, X, X, X, O, O
]

question_mark2 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
X, O, O, O, O, X, X, O,
O, X, O, O, X, O, O, X,
O, O, X, O, X, O, O, O,
O, O, O, X, X, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

question_mark2_1= [
X, X, X, O, O, X, X, X,
X, X, X, O, O, X, X, X,
X, X, X, O, O, X, X, X,
O, O, O, O, O, O, O, O,
O, O, O, X, X, O, O, O,
O, X, X, X, X, X, X, O,
O, X, X, O, O, X, X, O,
O, X, X, O, O, X, X, O
]

def main(args):
    sense = SenseHat()
    loc = 0
    toggle = 0
    event = 0
    
    temp = int(sense.get_temperature())
    hum = int(sense.get_humidity())
    pre = int(sense.get_pressure())
    
    if loc == 0 :
        sense.show_message("{0} {1} ".format(hum, 'rain'), text_colour = [255,50,255])
        sense.set_pixels(question_mark0)
    
    try:
        while True:
            if toggle == 0:
                event = sense.stick.wait_for_event()
                toggle+= 1
            elif toggle == 1:
                event = sense.stick.wait_for_event()
                toggle += 1
                continue
            elif toggle == 2:
                toggle = 0
                continue
                
            if toggle == 1:
                if event.direction == 'up' :
                    loc -= 1
                    if loc == -1 :
                        loc = 2
                elif event.direction == 'down' :
                    loc += 1
                    if loc == 3 :
                        loc = 0
                else :
                    continue
                
            temp = int(sense.get_temperature())
            hum = int(sense.get_humidity())
            pre = int(sense.get_pressure())
            
            if loc == 0 :
                sense.show_message("{0} {1} ".format(hum, 'rain'), text_colour = [255,50,255])
                sense.set_pixels(question_mark0)
            elif loc == 1 :
                sense.show_message("{0} {1} ".format(temp, 'good'), text_colour = [255,50,255])
                sense.set_pixels(question_mark1)
            elif loc == 2 :
                sense.show_message("{0}".format(pre), text_colour = [255,50,255])
                sense.set_pixels(question_mark2)
                time.sleep(2)
                sense.set_pixels(question_mark2_1)
            
            
            
    except KeyboardInterrupt:
        sense.clear(0, 0, 0)
        print(" ")
       
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
