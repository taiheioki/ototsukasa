﻿import subprocess

class Speaker:

	def __init__(self):
		pass

	# speed : 50-300
	def speak(self, text, speed = 100):
		subprocess.call("/home/pi/aquestalkpi/AquesTalkPi -v f2 -s " + str(speed) + " " + text + ' | aplay -D "hw:0,0"', shell = True)
