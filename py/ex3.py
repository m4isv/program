#criando uma class com construtor e variaveis internas

class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura


pessoa1 = Pessoa('Fernando', 32, 'M', 1.90)



print(pessoa1.nome, pessoa1.idade)

print(f'bem vindo {pessoa1.nome} parabens pelos seus {pessoa1.idade} Anos !!')
