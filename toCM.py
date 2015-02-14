import socket
import time
import pickle
import serial

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

LW_ID = 1
RW_ID = 2
rotation_mode = 0
position_mode = 1

#ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/tty/ACM0', 9600)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP from receive function CPU
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	L = pickle.loads(data)
	L[3] = VALUE

	if (L[0] == 'LW'):
		ID = LW_ID
	if (L[0] == 'RW'):
		ID = RW_ID
	if (L[1] == 'rotation'):
		MODE = rotation_mode
	if (L[1] == 'position'):
		MODE = position_mode
	print [ID,MODE,VALUE]

	#ser.write([ID,MODE,VALUE])	
	

	time.sleep(.01)
