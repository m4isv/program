numero = int(input("digite um numero\n"))

print(f"Analizando o Numero {numero}.....")

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f"unidade{u} dezena{d} centena{c} milhar{m}")