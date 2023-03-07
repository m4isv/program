
#property, getters, setters


class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def desconto(self, porcetual):
        self.preco = self.preco - (self.preco * (porcetual / 100))


    #getter
    @property
    def preco(self):
        return self._preco


    #setter
    @preco.setter

    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

produto1 = Produto('Camiseta', 99)
produto1.desconto(5)

print(produto1.preco)



produto2 = Produto('Calça', 'R$59')
produto2.desconto(15)
print(f'Produto2 apos aplicação do desconto terá valor de {produto2.preco}')


