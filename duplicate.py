import os

numFiles = 80
filenum = 3
suffix = ""
for filenum in range(1,96):
        filename = str(filenum)
        if filenum < 10:
                filename = "0" + str(filenum)
        #os.system(" mkdir d"+filename)
        #os.system(" mv x"+filename+" d"+filename)
        #os.system(" cp getResources.py d"+filename)
	
        cmd = " echo 'python getResources.py /export/home/bakerally/testsplit/d"+filename+"/x"+filename+" &' > /export/home/bakerally/testsplit/d"+filename+"/run"
        os.system(cmd)

        #cmd = "chmod +x /home/bakerally/testsplit/d"+filename+"/run"
        #os.system(cmd)
