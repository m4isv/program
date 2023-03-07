class Televisao:
	
	def __init__(self):
		self.ligada = False
		self.canal = 4
		
Tv = Televisao()

Tv.ligada = True

Tv.canal = 100

print(Tv.ligada, Tv.canal)