#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  adcread.py
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

import spidev
import time

SPI_CE = 0
POTEN_CHANNEL = 0

def main(args):
    spi=spidev.SpiDev()
    spi.open(0,SPI_CE)
    spi.max_speed_hz=1000000
    
    try:
        while True:
            adc=spi.xfer2([1, (8+POTEN_CHANNEL) << 4, 0])
            val=((adc[1]&0x03) << 8) + adc[2]
            print("Potentionmeter is {0}".format(int(val)) )
            time.sleep(0.5)
            
            
    except KeyboardInterrupt:
        spi.close()
        
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
