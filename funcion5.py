def frec(numero, digito):
    sd = 0
    cd = str(numero)
    for x in cd: 
        if x == str(digito):
            sd = sd + 1
    return sd


numero1 = int(input('Ingrese número entero: '))
digito1 = int(input('Ingrese digito que deseas hallar dentro del número: '))

print(f'En el número {numero1} existen {frec(numero1, digito1)} digitos{digito1}')

