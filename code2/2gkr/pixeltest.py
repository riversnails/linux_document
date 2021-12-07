from sense_hat import SenseHat
import time

def main(args):
    sense = SenseHat()
    
    try:
        while True:
            temp = int(sense.get_temperature())
            hum = int(sense.get_humidity())
            pre = int(sense.get_pressure())
            sense.show_message("{0} {1} {2}".format(temp, hum, pre), text_colour = [temp,hum,0])
            #print("{0} {1} {2}".format(temp, hum, pre))
            time.sleep(3)
            
    except KeyboardInterrupt:
        sense.clear(0, 0, 0)
        print(" ")
       
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
