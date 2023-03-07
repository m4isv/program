from socket import getservbyport

porta1= 80
porta2 = 21
porta3 = 25
porta4 = 143
porta5 = 23
porta6 = 22
porta7 = 67
porta8 = 53

print(f"a porta {porta1} e {getservbyport(porta1)}")
print(f"a porta {porta2} e {getservbyport(porta2)}")
print(f"a porta {porta3} e {getservbyport(porta3)}")
print(f"a porta {porta4} e {getservbyport(porta4)}")
print(f"a porta {porta5} e {getservbyport(porta5)}")
print(f"a porta {porta6} e {getservbyport(porta6)}")
print(f"a porta {porta7} e {getservbyport(porta7)}")
print(f"a porta {porta8} e {getservbyport(porta8)}")