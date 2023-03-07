import socket
class Ip:
	def __init__(self,site=None):
		self.site = input("enter a site ex: www.google.com: ")
		
	def view(self):
		return socket.gethostbyname(self.site)
		
ip = Ip()
print(f"the ip from this site is {ip.view()}")