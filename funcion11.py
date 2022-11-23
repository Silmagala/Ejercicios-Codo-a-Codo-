def valido_dni(dni):
    cd = len(str(dni))
    if cd == 7 or cd == 8:
        return True
    return False

dni1 = int(input('Ingrese su dni: '))
if valido_dni(dni1):
    print(f'El dni {dni1} es valido')
else:
    print(f'El dni {dni1} es invalido') 




