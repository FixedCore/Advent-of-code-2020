from datetime import date
from shutil import copyfile
import os

day = int(date.today().strftime("%d"))

dir_path = "Day " + str(day)

if dir_path not in os.listdir():
	print("Creating!")
	os.mkdir(dir_path)
	f = open(dir_path + "\\input.txt", 'w')
	f.close()
	copyfile('template.py', dir_path + "\\solution1.py")
	copyfile('template.py', dir_path + "\\solution2.py")
else:
	print("Dir already exists")