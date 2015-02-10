import socket

UDP_IP_IN = "127.0.0.1"
UDP_IP_OUT = "127.0.0.1"
UDP_PORT_IN = 5005
UDP_PORT_OUT = 5006

sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP from Control CPU
sock_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP to serial interface process
sock_in.bind((UDP_IP_IN, UDP_PORT_IN))

while True:
	data, addr = sock_in.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
	
	sock_out.sendto(data, (UDP_IP_OUT, UDP_PORT_OUT))

	time.sleep(.01)