#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex.py
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

code = 10
import RPi.GPIO as GPIO

def main(args):
    
    """
    age=10
    name='asdf'
    job='student'
    msg='''abcdefghi
    jklmnopqrstuvwxyz'''
    
    print("age = ", age, type(age), id(age))
    print("job = ", job, type(job), id(job))
    print("msg = ", msg, type(msg), id(msg))
    
    print("age = %d" %age)
    print("job = %s, name = %s" %(job, name))
    
    print("age", 100, sep='', end='\t')
    
    global code
    
    print(code)
    code+=1
    print(code)
    
    '''value = input(": ")
    print(value, type(value))'''
    
    print("len(msg) = %d", len(msg))
    print("msg[0] = %s, msg[-1] = %s" %(msg[0], msg[-1]))
    print("len(msg) = %s" %msg[1:6])
    
    print("msg.upper() = ", msg.upper())
    print("msg.split('') = ", msg.split('g'))
    print("'-'.join('sadf') = ", '-'.join('asdf'))
    
    print("{}year {}month {}day".format(2020, 10, 28))
    print("{1}year {2}month {0}day".format(2020, 10, 28))
    """
    
    data=['abc',1,2.21]
    data2=[]
    
    print("{}, {}, {}".format(data[0],data[1],data[2]))
    data2.append("good")
    data2.append(123.235)
    print("{}, {}".format(data2[0],data2[1]))
    data2[0] = 'asdfasfd'
    print("{}, {}".format(data2[0],data2[1]))
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
