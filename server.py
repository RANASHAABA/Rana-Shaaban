# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 09:43:13 2023

@author: User
"""

import socket 
import time
PORT=8080
HOST=""



s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creating the socket
s.bind((HOST,PORT))   #binding the socket to the port and the host inorder to make the connection 
s.listen()  #listening for incoming connections 

while True: 
    commun_socket, address= s.accept() #client socket 
    print(f"connected to {address}")  #print the address of the client 
    with commun_socket: 
     message= commun_socket.recv(1024).decode()# to get the request from the client 
     print(f"Recieved a request from:{address}: {message}")
     #now we need to get the destination server ip address from the request sent by the client 
     destination_address=message
     print(f"The destination server ip address is{destination_address}")
     print(time.time())
     request_String=f"GET / HTTP/1.1\r\nH ost:{destination_address}\r\n\r\n"
     print(request_String)
     try:
     
      #now we need to create a new socket to connect to the server 
      servsocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      servsocket.connect((destination_address,80)) #since we are accessing http webpages, the port numbeer should be 80 and the destination ip address is the one provided by  the client 
      #  the following lines of code correspondes to sending the request to the server and then recieving the response
      request_String=f"GET / HTTP/1.1\r\nH ost:{destination_address}\r\n\r\n"
      print(request_String) 
      servsocket.sendall(request_String.encode()) 
     
     
     #got this fuunction from google 
      print(f"The request has been sent to the address :{destination_address}")
      print(time.time())
      response=servsocket.recv(1024)
      print("The response is recieved now ")
     #now we send the response to the client 
      commun_socket.sendall(response)
      print("The response is now sent to the client!")
      print(time.time())
    
      print(f"Connection with {destination_address} has ended!".deocde())
      servsocket.close()
     except socket.error: 
                print("ERROR! ")
                error='HTTP/1.0 500 Internet server Error\n\n'.encode()
                commun_socket.send(error)

      
     commun_socket.close()
    
    
    
#The physical MAC address of my computer: 
    # AC-82-47-9B-88-C6
 

    
    
    
    
    
    

