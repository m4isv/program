import marshal

co = "print('hello mundo')"

c = compile(co, 'hello mundo', 'exec')

print(marshal.dumps(c))