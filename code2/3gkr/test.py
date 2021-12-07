#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2021  <pi@raspberrypi>
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


from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)
lcd.write_string('asdf')

data_list = '_test-123_asdf-235_we-456_'.split('_')
print(data_list)
for i in data_list :
    qwer = i.split('-')
    print(qwer)
    if any('asdf' in asdf for asdf in qwer) :
        print("qweqwr")
    #asdf = data_list.split('-')
    
