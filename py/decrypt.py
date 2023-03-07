import base64
nome = input("digite uma senha encryptada para descypta: ").encode()

cod = base64.standard_b64decode(nome)

print(f"a senha decryptada e \033[1;45m {str(cod).replace('b','')} \033[m")