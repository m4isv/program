#baixa imagens 

import requests

try:
	url = input("digite uma url de uma imagem.jpg   ")
	
	r = requests.get(url)

except:
	print("ocorreu um error")

else:
	with open('img.jpg', 'wb') as f:
		f.write(r.content)