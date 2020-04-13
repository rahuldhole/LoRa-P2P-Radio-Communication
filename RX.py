#!/usr/bin/python
# -*- encoding: utf-8 -*-
import time
import serial
import binascii
import base64
from time import sleep
import os
import textwrap
from subprocess import PIPE, Popen

sp = serial.Serial()
sp.port = 'COM10'
sp.baudrate = 57600
sp.parity = serial.PARITY_NONE
sp.bytesize = serial.EIGHTBITS
sp.stopbits = serial.STOPBITS_ONE
sp.dtr = 0
sp.open()

def send(data):
    sp.write((data+"\x0d\x0a").encode())
    data.rstrip()
    time.sleep(2)
    rdata=sp.read_all()
    rdata=rdata.decode("utf-8")
    return rdata

'''
print(sp.read_all().decode("utf-8"))
print("Resetting device : ")
print(send("sys reset"))

print("Getting system version")
print(send("sys get ver"))

print("Pausing mac LoRaWAN")
print(send("mac pause"))

print("Baseband data shaping 0.5")
print(send("radio set bt 0.5"))

print("Radio mod lora")
print(send("radio set mod lora"))

print("Frequency 869100000")
print(send("radio set freq 869100000"))

print("Radio power 14")
print(send("radio set pwr 14"))

print("Spreading factor sf7")
print(send("radio set sf sf7"))

print("Auto frequency bandwidth afcbw 41.7")
print(send("radio set afcbw 41.7"))

print("Signal receiving bandwidth rxbw 125")
print(send("radio set rxbw 125"))

print("FSK bitrate value 5kb/s (5000)")
print(send("radio set bitrate 5000"))

print("Frequency deviation fdev 25000")
print(send("radio set fdev 25000"))

print("Preamble length for Tx/Rx (prlen 8)")
print(send("radio set prlen 8"))

print("CRC header on")
print(send("radio set crc on"))

print("Invert IQ off")
print(send("radio set iqi off"))

print("Coding rate 4/5")
print(send("radio set cr 4/5"))
##
##Watchdog time = 0 disabble for continuous reception
##
print("Watchdog Time 60000ms (0 disabble for continuous reception)")
print(send("radio set wdt 60000"))

print("Syncing word 0x12")
print(send("radio set sync 12"))

print("Radio Bandwidth 125")
print(send("radio set bw 125"))
'''
#sp.write("mac pause\x0d\x0a".encode())
period=10
#sp.write("radio rx 0\x0d\x0a".encode())
i=0
flag=1
rda = ""

while True:
	if flag:
		sp.write("radio rx 0\x0d\x0a".encode())
		#time.sleep(0.2)
		print("yes")
		flag=0
	elif flag==0:
		m = sp.read_all().decode("utf-8")
		rda = rda+m
		if "7D7D" in rda:
			print(rda)
			kama = rda.split('7B7B')
			vidata = kama[1].split('7D7D')
			print(vidata[0])
			msg2 = bytes.fromhex(vidata[0]).decode('utf-8')
			print("Message Decoded: "+str(msg2))
			flag=1
			rda = ""
			m = ""
			kama = ""
		#elif rda.find('tx_error'):
			#flag=1
			#rda = ""
			#m = ""
			
			
	
	'''
	print("Radio received "+msg)
	print("Radio received "+msg)
	#if msg.startswith('radio_rx'):
	msg = msg.replace('radio_rx  ', '')
	print("Message: Replaced "+str(msg))
	#msg2 = bytes.fromhex(msg1).decode('utf-8')
	print("Message Decoded: "+str(msg))
	#else:
	print("No data in "+msg)
	'''
	#time.sleep(0.1)
	
	
'''
	m = sp.read_all().decode("utf-8")
	print("Channel "+str(i)+" : "+m)
	sp.write(("mac get ch dcycle "+str(i)+"\x0d\x0a").encode())
	i = i+1
	if i%15==0:
		i=0
'''