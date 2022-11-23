def maximo(a, b):
    if a > b:
        return a
    else:
        return b

def minimo(a, b):
    if a < b:
        return a
    else:
        return b

x = int(input('Un numero: '))
y = int(input('Otro numero: '))

print(maximo(x - 3, minimo(x + 2, y - 5)))