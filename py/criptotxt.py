import base64

link = "www.facebook.com/profile"

v = base64.urlsafe_b64encode(link)
print(v)

file = open("cript.tx","w")
file.write(v)
