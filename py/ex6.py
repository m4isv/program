#metodos estaticos
#aqueles que nao possui instacias como atributo, funciona como uma função normal dentro da class

from random import randint

class Pessoa:
    @staticmethod

    def gerador_id():
        gerador = randint(100, 999)

        return gerador


print(Pessoa.gerador_id())


