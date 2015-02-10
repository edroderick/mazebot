#!/usr/bin/env python

import curses
import socket

#initialize UDP Socket
UDP_IP = "192.168.1.145"	#static IP of raspberry pi
UDP_PORT = 5005
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

#intialize curses module
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(False)

# Get the current feed-forward (state) 
while (True):
 	#clear buffer to prevent overwhelming RasPI with UDP messages when directional keys held down
	curses.flushinp()
	inputKey = stdscr.getch()
	if inputKey == ord('x'): #exit on X key and close curses module and ach channel
		curses.nocbreak()
		stdscr.keypad(False)
		curses.echo()
		curses.endwin()
		break
	elif inputKey == curses.KEY_RIGHT:
		MESSAGE = "RIGHT"
	elif inputKey == curses.KEY_LEFT:
		MESSAGE = "LEFT"		
	elif inputKey == curses.KEY_UP:
		MESSAGE = "UP"		
	elif inputKey == curses.KEY_DOWN:
		MESSAGE = "DOWN"

	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

	time.sleep(.5)
