#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  blue.py
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

from bluetooth import *

try:
    socket = BluetoothSocket( RFCOMM ) #프로토콜 설정 
    socket.connect(("98:D3:31:90:76:68", 1)) #맥주소로 연결
    print("bluetooth connected!")

    while True:
        
        '''
        data = socket.recv(1024)
        print(data)
        '''
        
        input_data = input() #입력대기 후 소켓으로 날림 
        if input_data:
            socket.send(input_data)
        
            
        
except KeyboardInterrupt: #인터럽트시에 소켓을 닫음
    socket.close()
    sys.exit()
