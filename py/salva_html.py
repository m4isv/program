import requests

#Método post
url = 'http://www.faceboom.com'


response = requests.post(url)

with open('faceboom.html', 'w') as f:
	f.write(response.text)


