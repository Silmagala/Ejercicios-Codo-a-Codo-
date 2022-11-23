def triangulo(ancho, k):
    for y in range(1, ancho + 1): 
        for x in range(y):
            print(k, end =' ')
        print(' ')

def triangulo1(ancho, k):
    for y in range(1, ancho): 
        for x in range(ancho - y):
            print(k, end =' ')
        print(' ')

x = int(input('ancho: '))
k = str(input('Caracter a introducir: '))

triangulo(x, k)
triangulo1(x, k)