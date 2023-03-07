from socket import gethostbyname

class Site(object):
	def __init__(self,site):
		self.site = site
		self.ip = gethostbyname(site)
		

web = Site("www.xnxx.com.com")
	
print(web.site,web.ip)