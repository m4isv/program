from time import sleep
import os
for n in range(20):
	sleep(0.1)
	os.system("clear")
	print("\033[1;32mcarregando..\033[m")
	for b in range(0,n):
		print(f"\033[1;32m#\033[m",flush=True,end="")
	