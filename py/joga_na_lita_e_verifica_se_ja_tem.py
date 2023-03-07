
produtos = []

while True:
    produto = input("Informe um produto ou 0 para sair: ")
    
    if produto in produtos:
        print("PRODUTO JÁ ESTÁ NA LISTA!")
    
    elif produto == "0":
        break
        
    else:
        produtos.append(produto)

print(produtos)