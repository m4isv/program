
#metodos de class
#metodos que ate interagem com funçoes ,mas retorna dados para escopo global da class

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod
    def ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento

        return cls(nome,idade)

pessoa2 = Pessoa.ano_nasc('Fernando', 1987)

print(pessoa2.idade)

