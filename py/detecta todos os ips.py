#buscador de ip
import socket
from time import sleep

print("#"*40)
digite=str(input("\033[35m DIGITE UM SITE PARA VER TODOS OS  ip\n")).strip()
print("#"*40)
print("\033[36m Procurando..")
print("□□□□□0%")
sleep(2)
print("■■■■■□□20%")
sleep(4)
print("■■■■■■□□40%")
sleep(6)
print("■■■■■■■□□60%")
sleep(8)
print("■■■■■■■■□80%")
sleep(10)
print("■■■■■■■■■□90%")
sleep(17)
print("■■■■■■■■■■100%")
print("Detectado")
print("os ip do Site São",socket.gethostbyname_ex(digite) )
