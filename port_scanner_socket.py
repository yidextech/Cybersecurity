import sys
import socket
from datetime import datetime


print(r"""         _________ ______   _______          
|\     /|\__   __/(  __  \ (  ____ \|\     /|
( \   / )   ) (   | (  \  )| (    \/( \   / )
 \ (_) /    | |   | |   ) || (__     \ (_) / 
  \   /     | |   | |   | ||  __)     ) _ (  
   ) (      | |   | |   ) || (       / ( ) \ 
   | |   ___) (___| (__/  )| (____/\( /   \ )
   \_/   \_______/(______/ (_______/|/     \|
                                             """)

print("*"*45)

target = input(str("Target IP: "))
 
print("_"*45)
print("Scanning Traget: "+target)
print("Scanning started at: "+str(datetime.now()))
print("_"*45)


a,b = map(int, input("Enter port range you want to scan : e.g 80-80, 80-443: ").split("-"))
if a<1 or b>65535 or a>b:
    sys.exit("Please use the correct format for the port!")

try:
    for port in range(a, b+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting!")
    sys.exit()
except socket.error:
    print("\ Host not responding!")
    sys.exit()
else: 
    print("-"*45)
    print("\nScanning Completed!")
    print("*"*45)
