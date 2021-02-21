from ip2geotools.databases.noncommercial import DbIpCity
import re
from time import sleep
from urllib.request import urlopen
from json import load
from random import choice
import os, errno
active = False

try:
	os.makedirs("ip")
except FileExistsError:
	# directory already exists
	pass
try:
	while active == False:
		fileup = input("Enter name of file to save to sort | Example text.txt :")
		fileex = os.path.exists(fileup)

		if fileex:
			active = True
			datadd = []
			fileip = open("{}".format(fileup), "r")
			if fileip.mode == 'r':
				fileread = fileip.readlines()
				for linefile in fileread:
					datadd.append(linefile.replace("\n", ""))
			proxies={'http',choice(datadd)}
			print(proxies)

			def dft(ip):
				global datadd
				
				if ip == '':
					url = 'https://ipinfo.io/json'
				else:
					url = 'https://ipinfo.io/' + ip + '/json'
				res = urlopen(url)
				#response from url(if res==None then check connection)
				data = load(res)
				#will load the json response into data
				for attr in data.keys():
					#will print the data line by line
					sd =(attr,' '*13+'\t->\t',data[attr])
					if attr=="country":
						c=data[attr]
				print(c)
					
				return c

			#-------------------------------
			#Sort ip by geoip country code and saved to txt file check folder named /ip 
			txto = [fileup]
			data = []
			dactive = []
			wactive = []
			tim = 0
			#-------------------------------
			for f in txto:
				saas=open("{}".format(f), "r")
				if saas.mode == 'r':
					fch =saas.readlines()
					for xwo in fch:
						rop = re.search('(.*):', xwo).group(0).replace(':','')
						io=[dft(rop)]
						#sleep(2)
						#print("ip : "+str(io)+" : "+str(rop))
						if io[0] in data:
							af = data.index(io[0])
							data.insert(af, rop)
							print("IP added to "+str(io)+" database | Totale : "+str(len(data[af])))
							tim+=1
							
							qess="ip/"+str(io[0])+".txt"
							fdsss = open(qess,"a+")
							fdsss.write(xwo.replace('\n','')+"\n")
							#______________________/*
						else:
							if xwo in io[0]:
								pass
							else:
								
								qes="ip/"+str(io[0])+".txt"
								fdss = open(qes,"a+")
								fdss.write(xwo)
								#______________________/*
								data.append(io[0])
								
								print(data[0])
		else:print("file not found ")
except KeyboardInterrupt:
	print("programme close down checklist")
	exit(0)
