def digito(num):
    s = 0
    num1 = str(num)
    for x in num1:
        x1 = int(x)
        s = x1 + s
    return s
cd = 0
my = -9
mayor = 0
res = str(input('¿Deseas ingresar otro numero? s/n: '))
while res == 's':
    numero1 = int(input('Ingrese número positivo: ')) 
    if digito(numero1) < 10:
        cd = cd + 1
    else:
        if digito(numero1) > my:
            my = digito(numero1) 
            mayor = numero1     
    res = str(input('¿Deseas ingresar otro numero? s/n: '))

print(f'El numero cuya suma de digitos fue mayor que 10 es {mayor} ')
print(f'Cantidad de numeros cuya suma de digitos fue menor que 10 es {cd}')
