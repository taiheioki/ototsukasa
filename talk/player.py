import subprocess
import threading
import time

class Player:
	
	def __init__(self):
		thread = threading.Thread(target = target)
	
	def play(self, id):
		url = subprocess.check_output(["youtube-dl", "-g", "https://www.youtube.com/watch?v=" + id]).rstrip()
		p = subprocess.Popen(["omxplayer", "-o", "local", url])
	
	def target(self):
		time.sleep(25)
