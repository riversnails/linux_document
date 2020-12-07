from sense_hat import SenseHat
import time

O = [0, 0, 0]
X = [255, 50, 255] 

question_mark = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, X, O, O, X, O, O,
O, X, O, X, X, O, X, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, X, X, O, O, O
]

def main(args):
    sense = SenseHat()
        
    try:
        while True:
            temp = int(sense.get_temperature())
            hum = int(sense.get_humidity())
            pre = int(sense.get_pressure())
            #print("{0} {1} {2}".format(temp, hum, pre))
            sense.show_message("{0} {1} ".format(hum, 'sun'), text_colour = [255,50,255])
            sense.set_pixels(question_mark)
            #print("{0} {1} {2}".format(temp, hum, pre))
            time.sleep(2)
            
    except KeyboardInterrupt:
        sense.clear(0, 0, 0)
        print(" ")
       
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
