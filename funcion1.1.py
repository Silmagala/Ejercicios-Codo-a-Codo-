def rectangulo(anchura, altura):
    for y in range(altura): 
        for x in range(anchura):
            print('*', end ='')
        print(' ')

y = int(input('altura: '))
x = int(input('anchura: '))

rectangulo(x, y)
