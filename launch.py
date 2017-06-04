import os
import sys

numFiles = 80
filenum = 3
suffix = ""
start = 9
stop = 95 + 1
status = sys.argv[1]

if len(sys.argv) > 2:
	start = int(sys.argv[2])

if len(sys.argv) > 3:
	stop = int(sys.argv[3]) + 1

for filenum in range(start,stop):
	filename = str(filenum)
	if filenum < 10:
		filename = "0" + str(filenum)
	
	if status == "run":
		os.system(" cd d"+filename+"; ./run &")
		os.system(" cd ..")
	
	if status == "counter":
		os.system(" tail d"+filename+"/counter ")
	#os.system(" cp rm d"+filename)
	#os.system(" cd d"+filename+"; ./rm &")
