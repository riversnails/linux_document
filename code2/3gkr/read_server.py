"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import picamera as camera
import time

port = 8888
count = 0

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
	count = 0
	def do_GET(self):
		count = 0
		if self.path == "/camera":
			cam = camera.PiCamera()
			cam.start_preview()
			cam.capture("/home/pi/Desktop/cam.jpg")
			cam.stop_preview()
			cam.close()
		print(self.path);
		self.send_response(200)
		self.send_header('Content-Type', 'text/html; charset=utf-8')
		self.end_headers()
		self.wfile.write('<h1>Hello</hi>'.encode('utf-8'))
		
httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
print(f'Server running on port:{port}')
httpd.serve_forever()
"""

import picamera as camera
import socket
from RPLCD.i2c import CharLCD


HOST = '192.168.0.71'
PORT = 8888   

pysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try :
	pysocket.bind((HOST, PORT))
except :
	print("bind failed!")
	exit()


cam = camera.PiCamera()
lcd = CharLCD('PCF8574', 0x27)
pysocket.listen()
print("init finish")
(client_socket, addr) = pysocket.accept()
print("connected")

count = 0
video_count = 0

try :
	while True:
		data = client_socket.recv(1024)
		str1 = data.decode()
		print(str1)
		
		data_list = str1.split('_')
		
		for i in data_list :
			data_list2 = i.split('-')
			
			if any('TEMP' in var for var in data_list2) :
				v = 'tp:' + data_list2[1]
				lcd.cursor_pos=(0,0)
				lcd.write_string(v)
				
			elif any('HUMI' in var for var in data_list2) :
				v = 'hi:' + data_list2[1]
				lcd.cursor_pos=(0,8)
				lcd.write_string(v)
			elif any('BRIT' in var for var in data_list2) :
				v = 'bright:' + data_list2[1]
				lcd.cursor_pos=(1,0)
				lcd.write_string(v)
				
		if any('CAME-ON' in var for var in data_list) :
			cam.start_preview()
			cam.start_recording("/home/pi/video{}.h264".format(video_count))
			video_count += 1
		if any('CAME-OFF' in var for var in data_list) :
			cam.stop_preview()
			cam.stop_recording()
			
	'''	
		if str1 == "button" :
			print("camera on")
			cam = camera.PiCamera()
			cam.start_preview()
			char = "/home/pi/Desktop/cam{}.jpg".format(count)
			count += 1
			cam.capture(char)
			cam.stop_preview()
			cam.close()
			'''
except :
	client_socket.close()
	pysocket.close()
