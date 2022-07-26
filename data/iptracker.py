import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    def start():
        print (G+ '''\n==========IP Tracker==========''')
        main()        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print(Y+"\n==========Info gathered==========")
                #print(G+"[1] IP Address : "+Y,data['query'])
                print(G+"[1] Country:"+Y,data['country'])
                print(G+"[2] Region:"+Y,data['regionName'])
                print(G+"[3] City:"+Y,data['city'])         
                print(G+"[4] Org:"+Y,data['org'])
                print(G+"[5] Lattitude:"+Y,data['lat'])
                print(G+"[6] Longitude:"+Y,data['lon'])
                l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
                print(G+"[7] Google Map link:"+CY,l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n>>"+Y+" Open link in browser?"+G+" (y|n): "+W)
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                    elif pr=="n":
                        print("\nCheck another IP or exit using Ctrl + C\n\n")
                        start()
                    else:
                        print("\nInvalid choice! Please try again\n")
                else:
                    pr=input(R+"\n>>"+Y+" Open link in browser?"+G+" (y|n): "+W)
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                    elif pr=="n":
                        print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        print(Y+"\nCheck another IP or exit using "+R+"Ctrl + C\n\n")
                        start()
                    else:
                        print(R+"\nInvalid choice! Please try again\n")
                return
            except KeyError:
                print(R+"\nError! Invalid IP/Website Address!\n"+W)
                
        except urllib.error.URLError:
            print(R+"\nError!"+Y+" Please check your internet connection!\n"+W)
            exit()
        
    def main():
        u=input(Y+"\nEnter IP or website address:"+W+" ")
        if u=="":
            print(R+"\nEnter valid IP Address/website address!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
    start()
except KeyboardInterrupt:
    print(Y+"\nInterrupted ! Have a nice day :)"+W)
    