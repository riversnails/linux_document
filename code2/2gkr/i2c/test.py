#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
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

import RPi_I2C_driver as i2c
import time

LCD_ADDR = 0x27

def main(args):
    lcd = i2c.lcd(LCD_ADDR)
    
    try:
        while True:
            lcd.clear()
            lcd.print("Hello, ")
            time.sleep(1)
            
            lcd.print(" World", 0.5)
            time.sleep(1)
            
            for i in range(16):
                lcd.scrollDisplayRight()
                time.sleep(0.4)
                
            for i in range(16):
                lcd.scrollDisplayLeft()
                time.sleep(0.4)
                
    except KeyBoardInterrupt:
        print(" KeyboardInterrupt")
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
