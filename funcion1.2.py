def rectangulo(anchura, altura, k):
    for y in range(altura): 
        for x in range(anchura):
            print(k, end =' ')
        print(' ')

y = int(input('altura: '))
x = int(input('anchura: '))
k = str(input('Caracter a introducir: '))

rectangulo(x, y, k)