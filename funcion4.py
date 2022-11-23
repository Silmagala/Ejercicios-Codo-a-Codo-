def primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

numero = int(input('Ingrese número: '))

if primo(numero):
    print(f'{numero} es primo ')
else:
    print(f'{numero} no es primo ')
