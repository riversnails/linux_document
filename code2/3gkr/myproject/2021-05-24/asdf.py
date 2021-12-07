from bluetooth import *

past_str = "T"

try:
	socket = BluetoothSocket( RFCOMM )
	socket.connect(("98:D3:91:FD:F6:EA", 1))
	print("bluetooth connected!")


	while True:
		data = socket.recv(1024)
		str1 = data.decode()

		str2 = past_str + str1

		if "TEMP" in str2:
			print(str2)
		else:
			print(str1)
			past_str = str1

		'''
		input_data = input() #입력대기 후 소켓으로 날림 
		if input_data:
			socket.send(input_data)
		'''


except KeyboardInterrupt: #인터럽트시에 소켓을 닫음
    socket.close()
    sys.exit()
