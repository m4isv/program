import hashlib
m = hashlib.sha256()
m.update("oi".encode())

print(m.hexdigest())


from hashlib import sha512

print(sha512('oi'.encode()).hexdigest())

import hashlib
m = hashlib.sha256()
m.update("oi".encode())

print(m.hexdigest())