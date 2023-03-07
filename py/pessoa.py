class Pessoa:
    def __init__(self, name, age, sexo):
        self.name = name
        self.age = age
        self.sexo = sexo


maria = Pessoa("Maria", 18, "FEMININA")

print(maria.name, maria.age, maria.sexo)
