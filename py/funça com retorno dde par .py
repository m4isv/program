def par(n=0):
	if n % 2 ==0:
		return True
	else :
		return False


num = int(input("digite um numero\n"))
if par(num):
	print("E par")
else:
	print("Nao e par")