import socket
import time
import pickle
import serial

UDP_IP_IN = "192.168.1.245"
#UDP_IP_IN = "127.0.0.1"
#UDP_IP_OUT = "192.168.1.245"
UDP_PORT_IN = 5005
#UDP_PORT_OUT = 5006

ser = serial.Serial('/dev/ttyAMA0', 57600)
#ser = serial.Serial('/dev/ttyACM0', 9600)

sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP from Control CPU
#sock_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP to serial interface process
sock_in.bind((UDP_IP_IN, UDP_PORT_IN))

while True:
	data, addr = sock_in.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
	
	if (data == "F"):
		ser.write(chr(70))
	if (data == "B"):
		ser.write(chr(66))
	if (data == "L"):
		ser.write(chr(76))
	if (data == "R"):
		ser.write(chr(82))
	if (data == "S"):
		ser.write(chr(83))
	time.sleep(.05)
