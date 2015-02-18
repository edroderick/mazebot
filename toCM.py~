import socket
import time
import pickle
import serial

UDP_IP = "192.168.1.245"
UDP_PORT = 5006

LW_ID = "2"
RW_ID = "1"
wheel_mode = "0"
position_mode = "1"

ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/tty/ACM0', 9600)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP from receive function CPU
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	data2, addr2 = sock.recvfrom(1024) 

	L = pickle.loads(data)
	L2 = pickle.loads(data2)
	VALUE_1 = str(L[2])
	VALUE_2 = str(L2[2])

	if (L[0] == 'LW'):
		ID_1 = LW_ID
	if (L[0] == 'RW'):
		ID_1 = RW_ID
	if (L[1] == 'wheel'):
		MODE_1 = wheel_mode
	if (L[1] == 'position'):
		MODE_1 = position_mode
	if (L2[0] == 'LW'):
		ID_2 = LW_ID
	if (L2[0] == 'RW'):
		ID_2 = RW_ID
	if (L2[1] == 'wheel'):
		MODE_2 = wheel_mode
	if (L2[1] == 'position'):
		MODE_2 = position_mode
	packet = ID_1 + MODE_1 + VALUE_1 + ID_2 + MODE_2 + VALUE_2
	print packet
	ser.write(packet)	
	time.sleep(.05)
