import  hashlib
ip = hashlib.sha256()

ip.update(b"127.0.0.1: 1234")

print(ip.hexdigest())

