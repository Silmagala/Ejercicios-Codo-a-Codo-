def primo(numero):
    for x in range(2, numero):
        if numero % x == 0:
            return False    
    return True

def suma_dig(numero):
    sd = 0
    x1 = 0
    num = str(numero)
    for x in num:
        x1 = int(x)
        sd = sd +  x1
    return sd

def can_digito(numero, digito):
    cd = 0
    num = str(numero)
    for x in num:
        if int(x) == digito:
            cd = cd + 1
    return cd 

def fac(numero):
    f = 1
    for x in range(2, numero + 1):
        f = f * x
    return f
#for x in range(1, 6):
mayor = - 9
numero1 = int(input('Numero primo: '))
digito  = int(input('Ingrese digito: '))

while primo(numero1):
    print(f'Suma de digitos del numero: {numero1} es {suma_dig(numero1)}')
    print(f'Cantidad de veces que digito {digito} en {numero1} es {can_digito(numero1, digito)} ')
    if numero1 > mayor:
        mayor = numero1

    numero1 = int(input('Numero primo: '))
    digito  = int(input('Ingrese digito: '))

    print(f'El mayor numero es {mayor}')
    print(f'El factorial del numero mayor es {fac(mayor)}')