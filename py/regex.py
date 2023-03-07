import re

p = re.compile(r'[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}')

def validNumber(n):
    if re.fullmatch(p, n):
      return True
    
    else:
        print('Número inválido.')
        return False

print(validNumber('538.614.567-89'))