#! /usr/bin/env python
import RPi.GPIO as gp
from socket import *
from time import ctime
import os
import sys
import time
import datetime

houry = [6,7,8,9,10,11,12,13,14,15,16,17] #Adding hours.


savePathStr ='/home/test/image/' # root folder
os.system('sudo mkdir -p  ' + savePathStr)

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)

while True:
	if datetime.datetime.now().hour in houry:
		now = datetime.datetime.now()
		print (now)
		strBufDate = '%d%02d%02d' % (now.year,now.month,now.day) 
		print (strBufDate)

		strBufTime = '%02d' % (now.hour)
		strBufMin = '%02d' % (now.minute)
		strBufSec = '%02d' % (now.second)
		strBuf = '%s_%s%s%s.png' % (strBufDate,strBufTime,strBufMin,strBufSec)
		
		#multiplex setup for cam 1
		print ("Start testing the camera A")
		i2c = "i2cset -y 1 0x70 0x00 0x04"
		os.system(i2c)
		gp.output(7, False)
		gp.output(11, False)
		gp.output(12, True)
		os.system('sudo raspistill  -n -o '+savePathStr+"C1_"+"NoIR_"+"550F_"+strBuf) 

		
		#multiplex setup for cam 2
		print("Start testing the camera B")
		i2c = "i2cset -y 1 0x70 0x00 0x05"
		os.system(i2c)
		gp.output(7, True)
		gp.output(11, False)
		gp.output(12, True)
		os.system('sudo raspistill -n -o '+savePathStr+"C2_"+"NoIR_"+"1070F_"+strBuf) 
		
		#multiplex setup for cam 3
		print ("Start testing the camera C")
		i2c = "i2cset -y 1 0x70 0x00 0x06"
		os.system(i2c)
		gp.output(7, False)
		gp.output(11, True)
		gp.output(12, False)
		os.system('sudo raspistill -n -o '+savePathStr+"C3_"+"RGB_"+strBuf) 
		
		#multiplex setup for cam 4
		print("Start testing the camera D")
		i2c = "i2cset -y 1 0x70 0x00 0x07"
		os.system(i2c)
		gp.output(7, True)
		gp.output(11, True)
		gp.output(12, False)
		os.system('sudo raspistill -n -o '+savePathStr+"C4_"+"NoIR_"+"725F_"+strBuf) 
	else :
		continue
		sleep(43200) # wait for 12 hours for next day 6 am
	
	#time.sleep(120) # time in secs  (every 2min) eg: 9 am - 5 pm (...images)
	time.sleep(1800) # time in secs  (every 30min) eg: 9 am - 5 pm (...images)		
