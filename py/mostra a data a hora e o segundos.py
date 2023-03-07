from datetime import datetime

today = datetime.now()
dia = today.day
mes = today.month
ano = today.year
hora = today.hour
minuto = today.minute
segundo = today.second
print (f"o dia de hoje e {dia}/{mes}/{ano}")
print(f"as horas sao {hora}:{minuto}:{segundo} segundos")
