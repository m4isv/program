#detector de ip
import socket
from time import sleep
digite=input("digite um site para ver o ip ")
print("Analizando....")
sleep(3)
print(" o ip do site e" ,socket.gethostbyname(digite))