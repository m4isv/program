#Trabalhando com textos

#importar bibliotecas
import os
import sys
import glob

#lista de arquivos txt
lista_arq = []

#função limpar
def limpar():
    os.system('cls' if os.name == "nt" else "clear")
    
def listar():
    #tratamento de erro
    all_file = []

    for file in glob.iglob("*.txt"):
        all_file.append(file)

    if(all_file == []):
        print("Todos os arquivos criados.\n{}".format("-"*70))
        print("Não existe nenhum arquivo criado!")
        print("{}".format("-"*40))
    else:
        print("Todos os arquivos criados.\n{}".format("-"*40))
        print(all_file)
        print("{}".format("-"*40))
        

#para pausar sem lemite    
def pause():
    input("Preciona qualquer tecla para continuar")


#para fechar a função
def sair():
    return sys.exit()


limpar()#limpar tela antes de começar o algoritmo


#função escrever
def escrever():
    limpar()
    nome_arq = str(input("Insira um nome para arquivo: "))
    arq = open(nome_arq+".txt", "w")
    
    arq.write(input("Escreva um texto: \n"))
    
    arq.close()#fechamento de texto
    
#função modificar
def modificar():
    limpar()
    listar()
    valor = str(input("Queres modificar ou remover arquivo?: "))
    
    if((valor).lower() == "remover"):
        qual_1 = str(input("Insira nome do arquivo a ser removido: "))
        if(qual_1 == ""):
            pass
        else:
            os.system('cls' if os.name == "nt" else "rm -r "+qual_1+".txt")
    elif((valor).lower() == "modificar"):
        qual_2 = str(input("Insira nome do arquivo a ser modificado: "))
        if(qual_2 == ""):
            pass
        else:
            arq = open(qual_2+".txt", "a+")
            conteudo = str(input("Escreva texto: "))
            if(os.path.getsize(qual_2+".txt") > 0):
                arq.write("\n"+conteudo)
                return#fechar o algoritmo depois de escrever o conteúdo, caso o arquivo tenha mais que 0kb
            arq.write(conteudo)
        arq.close()
    else:
        print("Escreva uma das opções, modificar ou remover.")
        pause()
    
    
#função imprimir os texto na tela
def imprimir():
    limpar()
    listar()
    
    try:
        nome_arq = str(input("Insira nome do arquivo que desejas ver: "))
        arq = open(nome_arq+".txt", "r")
        print(arq.read())
    except OSError:
        print("Não existe nenhum diretorio com esse nome")
        

#função para saber se tem algo que usuário escreveu que está no arquivo
def pesquisar():
    limpar()
    listar()
    try:
        nome_arq = str(input("Qual dos arquivos queres pesquisar palavras: "))
        arq = open(nome_arq+".txt", "r")
        qual = str(input("Qual palavra queres pesquisar: "))
        for x in arq:
            lista_arq_texto = x.split()
            for y in lista_arq_texto:
                if(qual == y):
                    print(f"A palavra {y} está contida na frase.")
                    pause()
                    return
        print("Não existe nenhuma palavra com esse nome no texto...")
    except OSError:
        print("Não existe nenhum arquivo com esse nome...")
    pause()

#função mãe e controladora
def main():
    limpar()
    print(f"""
    1 Escrever um texto
    2 Ver texto
    3 Modificar
    4 Pesquisar
    5 Sair""")
    
    while True:
        try:
            valor = int(input("    insira um valor: "))
            if(valor == 1):
                escrever()
                main()
            elif(valor == 2):
                imprimir()
                print("\n\n\n")
                pause()
                main()
            elif(valor == 3):
                modificar()
                main()
            elif(valor == 4):
                pesquisar()
                main()
            elif(valor == 5):
                limpar()
                sair()
            break
        except ValueError:
            print("Ooops! Tem que ser número!")
    
main()#mãe da funções