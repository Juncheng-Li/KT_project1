a = ['like', 'array\n']
b = ['array\n', 'sick\n']

for element in b:
    print(b in a)

for e in range(0, len(b)):
    print(b[e] in a)