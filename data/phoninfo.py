import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import timezone
from phonenumbers.phonenumberutil import (region_code_for_country_code, region_code_for_number, country_code_for_region)
import pytz
from datetime import datetime
import re
import os, sys
#Define colors
G='\033[32m'
Y='\033[33m'
W='\033[37m'
#Banner
print(G+'''\n#==========PhonInfo==========#''')
try:
 try:
  num = input(W+"\nEnter number: ")
  #####Gether all information posible#####
  pn = phonenumbers.parse(num)
  country= geocoder.country_name_for_number(pn, "en")
  city= geocoder.description_for_number(pn, 'en')
  carrier= carrier.name_for_number(pn, 'en')
  timezone= timezone.time_zones_for_number(pn)
  isocode=region_code_for_country_code(pn.country_code)
  ccode=country_code_for_region(isocode)
  #Get time of time zone
  st=str(timezone)
  cat=st.translate(str.maketrans({'(': ' ', ')': ' ',',':' '}))
  cut=cat.replace("'", " ")
  var=cut.replace(" ", "")
  tz=pytz.timezone(var)
  now=datetime.now(tz)
  time=now.strftime('%I:%M:%S %d/%m/%Y')
  #Check if it's possible
  if phonenumbers.is_possible_number(pn):
    info=" This number is valid and possible\n"
  else:
    info=" This number is not valid nor possible\n"
    #Print information
  print(Y+"\n==========Info gathered==========")
  print(G+"[1] Country found: "+str(country)+" (+"+str(ccode)+")")
  print("[2] City/area: "+str(city))
  print("[3] Carrier: "+str(carrier))
  print("[4] Time zone: "+str(var))
  print("[5] Current time: "+str(time))
  print("[6]"+W+info)
  from data.config import *
 except:
    print("\nEnter a valid number with country code.\n")
    from data.config import *
except KeyboardInterrupt:
	print("\nHave a nice day")