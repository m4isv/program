nome = "mARIA"
nome2 = "meu\tnome\tcom 4 cractere"
string = "isso e uma string"

print(nome.capitalize())
print(nome.casefold())
print(nome.center(20))
print(nome.count("m"))
print(nome.encode())
print(nome.endswith("A"))
print(nome2.expandtabs(19))
print(nome.find("A"))
print("meu nome e",format(nome))
print(nome.index("A"))
print(nome.isalnum())
print(nome.isalpha())
print(nome.isascii())
print(nome.isdecimal())
print(nome.isdigit())
print(nome.isidentifier())
print(nome.islower())
print(nome.isnumeric())
print(nome.isprintable())
print(nome.isspace())
print(nome.istitle())
print(nome.isupper())
nome = "-"
print(nome.join("mARIA"))
print(nome.lower())

print(string.ljust(20,"-"))
print(string.lstrip())