x = [x for x in range(100)]
print(x)
y = [pares for pares in x if pares%2 ==0]
print("os pares são\n{}".format(y))