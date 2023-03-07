from socket import gethostbyname

class Site(object):
	site = "www.google.com"
	ver = gethostbyname(site)