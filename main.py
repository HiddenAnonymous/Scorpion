import os, sys
import json
import urllib.request
import webbrowser

#Define colors
G='\033[92m'
GB='\033[1;32;40m'
os.system("rm -rf ")
os.system("clear")
print(G+"-----------------------------------------------")
print(G+'''          .<==+.
               \\  SCORPION
  __  /*-----._//
  >_)='-[[[[---' ''')
print(G+"-----------------------------------------------")


help= """\nThis tool is to get information from any target of its phone number or ip address besides of two DDoS attacks, by website domain name or ip address. 

By Hidden Anonymous
Youtube:  https://youtube.com/channel/UCcdAplf18AQ02f1mnOinP_g"""

try:
 choice=input(G+'''
1) Phoninfoga
2) IP Tracker
3) Ddosite
4) Ddosip
5) Help
6) Exit

Choose option: ''')

 if choice=="1":
  from data.phoninfo import *
 elif choice=="2":
  from data.iptracker import *
 elif choice=="3":
  from data.ddosite import *
 elif choice=="4":
  from data.ddosip import *
 elif choice=="5":
  print(help)
  input("\nType y to exit: ")
  os.system("python main.py")
 elif choice=="6":
  os.system("exit")
  print("\nGoodbye :)\n")
 else:
  os.system("python main.py")
  
except KeyboardInterrupt:
	print("\nHave a nice day :)\n")
