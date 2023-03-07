import requests


cnpj = ("13724914000147")
api =  requests.get("https://www.receitaws.com.br/v1/cnpj/"+cnpj).json()

for base in api:
  print(f"{base}: {api[base]}")