#mais de uma função dentro de uma class


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def ano_nascimento(self):
        ano_nasc = self.ano_atual - self.idade

        print(f'seu ano de nascimento e {ano_nasc}')


pessoa1 = Pessoa('Fernando', 32)

print(pessoa1.ano_nascimento())



