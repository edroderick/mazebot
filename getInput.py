#!/usr/bin/env python

import sys
import time
import numpy as np
from ctypes import *
import curses
import socket

#initialize UDP Socket
UDP_IP = "192.168.1.145"	#static IP of raspberry pi
UDP_PORT = 5005
#MESSAGE = "Hello, World!"
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
sock = socket.socket(socket.AF_INET, # Internet 
			socket.SOCK_DGRAM) # UDP

#intialize curses module
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(False)

lastkey = 0

# Get the current feed-forward (state) 
while (True):
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
		lastkey = inputKey
	elif inputKey == curses.KEY_LEFT:
		MESSAGE = "LEFT"	
		lastkey = inputKey	
	elif inputKey == curses.KEY_UP:
		MESSAGE = "UP"		
		lastkey = inputKey
	elif inputKey == curses.KEY_DOWN:
		MESSAGE = "DOWN"
		lastkey = inputKey

	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

	time.sleep(.5)
