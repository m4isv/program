
print('qual o Salario do Funcionario? R$')
salario = io.read()

print(math.float(salario))

novo = salario + (salario * 15/100)

print('um Funcionario que Ganhava '..salario,' Com 15% de Aumento Vai Ganha '..novo)


