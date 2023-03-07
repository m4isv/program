
import threading


def tarefa1():
 x = 0
 while x <20:
  print('funcao X', x)
  x+=1
  

def tarefa2():
 y = 0
 while y <20:
  print('funcao Y', y)
  y+=1


threading.Thread(target=tarefa1).start()

tarefa2()