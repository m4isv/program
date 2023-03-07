def abre_cor(a = "\033[1;41;44m"):
	print(a)
	
def feixa_cor(b = "\033[m"):
	print(b)
	
from socket import gethostbyname as detecta

from socket import gethostbyname_ex as todos


site = input("  digite um site\n  ").strip()

visualiza = detecta(site)

abre_cor()
print(f"  o ip do site e: \033[7;44;41m{visualiza} \033[m  ")
feixa_cor()


resposta = input(f"  quer ver todos os ip do site \033[1;41;44m{site}\033[m  S/N?  ")
if resposta[0].upper() in "S":
	abre_cor()
	print(todos(site))
	feixa_cor()

else:
	print("   ok, chauu   ")
	