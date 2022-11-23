def fac(numero):
    f = 1   
    for x in range(2, numero + 1):
        f = f * x 
    return f

def can_num():
    cn = 0
    res = str(input('¿Deseas ingresar otro numero? s/n: '))
    while res == 's':
        numero1 = int(input('Ingrese número: '))    
        cn += 1
        print(f'El factorial de {numero1} es {fac(numero1)} ')
        res = str(input('¿Deseas ingresar otro numero? s/n: '))
    return cn

print(f'Cantidad de numero leidos: {can_num()}')
