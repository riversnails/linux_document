import time
import spidev
import RPi_I2C_driver as i2c

SPI_CE = 0
POTEN_CHANNEL = 0

def main(args):
    spi = spidev.SpiDev()
    spi.open(0, SPI_CE)
    spi.max_speed_hz = 1000000
    lcd = i2c.lcd(0x27)

    try:
        while True:
            adc = spi.xfer2([1, (8 + POTEN_CHANNEL) << 4, 0])
            val = ((adc[1] & 0x03) << 8) + adc[2]
            print("Potentionmeter is {0}".format(int(val)))
            time.sleep(2)
            lcd.clear()
            lcd.print("analog:{0}".format(val))
    except KeyboardInterrupt:
        spi.close()
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    
