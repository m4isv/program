
--pegar pedaços
txt = 'hello world'

print(string.sub(txt, 1,5))

--conta
print(string.len('hello world'))
print(#'hello')

--maiscula
txt2 = 'hello'
print(string.lower(txt2))
print(string.upper(txt2))



--repeti
print(string.rep('A', 9))

--reverse

print(string.reverse("maria"))


email = "maria@gmail.com"

print(string.find(email, 'gmail'))
print(string.match(email, '@gmail.com'))

name = "eu quero maças"

resultado = string.gsub(name, 'maças', 'laranjas' ,1)
print(resultado)

