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
sp.port = '/dev/ttyUSB0'
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

period = 10
i=0
while True:
    print("Pausing mac LoRaWAN")
    #print(send("mac pause"))
    msg = "{{Hello "+str(i)+" Ravhlya}}"
    #print(sp.read_all().decode("utf-8"))
    msg = msg.encode().hex()
    print("Radio transfer "+str(msg))
    print(send("radio tx "+str(msg)))
    i=i+1
    if i%10==0:
        i=0
    time.sleep(period)
