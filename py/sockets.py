import socket

#print(socket.gethostbyname("www.python.org"))
"""Traduza  um  nome  de  host  para  o  formato  de  endereço  IPv4.  O  endereço  IPv4  é  retornado como  uma  sequência,  como '100.50.200.5'  .  Se  o  nome  do  host  for  um  endereço  IPv4,  ele será  retornado  inalterado.  Veja  gethostbyname_ex  ()  para  uma  interface  mais  completa. gethostbyname  ()  não  suporta  resolução  de  nomes  IPv6  e  getaddrinfo  ()  deve  ser  usado para suporte a pilha dupla IPv4 / v6."""


print(socket.gethostbyname_ex("www.python.org"))
"""Traduza  um  nome  de  host  para  o  formato  de  endereço  IPv4,  interface  estendida.  Retornar um  triplo (hostname,  aliaslist,  ipaddrlist)  ,  onde  hostname  é  o  nome  do  host  primário responder  ao  dado  ip_address  ,  aliaslist  é  uma  lista  (possivelmente  vazio)  de  nomes  de host  alternativos  para  o  mesmo  endereço,  e  ipaddrlist  é  uma  lista  de  endereços  IPv4  para o  mesma  interface  no  mesmo  host  (geralmente,  mas  nem  sempre,  um  único  endereço). gethostbyname_ex  ()  não  suporta  resolução  de  nomes  IPv6  e  getaddrinfo  ()  deve  ser usado para suporte a pilha dupla IPv4 / v6."""
