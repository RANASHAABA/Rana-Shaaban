# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:19:13 2023

@author: User
"""
import socket
import time
import uuid
Host= '127.0.0.1'
port=8080


newsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newsocket.connect((Host,port))  #to connect to the proxy server 
request_string= input("Please enter the website IP you want to access: ")
#start_time=datetime.time()
newsocket.sendall(request_string.encode())
start_time=time.time()
print(f"Now sending {request_string} to the proxy server, time: {start_time}")

response=newsocket.recv(1024).decode()
endtime=time.time()
print(f"The response is:{response} , time: {endtime}")
total=endtime-start_time
print(f"The total round-trip time:{total}")
#to get the MAC address we use the following function: 
  #from geeksforgeeks
print ("The MAC address in formatted way is : ", end="") 
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
newsocket.close()


