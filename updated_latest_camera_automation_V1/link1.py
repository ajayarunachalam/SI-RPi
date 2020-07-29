from os import system
import datetime
from time import sleep


def run():
	system('python3 test.py')
rest_sec=6

houry = [6,7,8,9,10,11,12,13,14,15,16,17]

while 1:
	if datetime.datetime.now().hour in houry:
		run()
	else :
		continue
		sleep(43200) # wait for 12 hours
	sleep(rest_sec)
