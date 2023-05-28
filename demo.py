from scapy.all import *
import socket
i = 1

while True:
   IP1 = IP(src = '120.20.20.5', dst = '220.20.30.5')
   TCP1 = TCP(sport = 70,dport = 80)
   pkt = IP1 / TCP1
   send(pkt)
   
   print ("packet sent ", i)
   i = i + 1
