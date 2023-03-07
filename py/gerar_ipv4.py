import ipaddress

def gerar_ip(ip):
	return ipaddress.IPv4Address(ip)

print(gerar_ip(3232235521))