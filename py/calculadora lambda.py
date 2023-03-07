soma = lambda n1,n2: n1+n2
subtrai = lambda n1,n2: n1-n2
mult= lambda n1,n2: n1*n2
dividi = lambda n1,n2: n1/n2
rest = lambda n1,n2: n1%n2


n1 = int(input("\t numero1: "))
n2 = int(input("\t numero2 "))

print(f"a soma é {soma(n1,n2)} ")
print(f"a subtração e {subtrai(n1,n2)} ")
print(f"a multiplicação é {mult(n1,n2)} ")
print(f"a divisão é {dividi(n1,n2)} ")
print(f"o resto da divisão e {rest(n1,n2)}")