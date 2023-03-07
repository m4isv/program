import base64

senha = input("digite uma senha: ")

date = bytes(senha,"ascii")

ver = base64.b64encode(date)

print(f"sua senha encryptada e \033[45m{str(ver).replace('b','')}\033[m")