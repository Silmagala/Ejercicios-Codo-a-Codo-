def valido_dni(dni):
    cd = len(str(dni))
    if cd == 7 or cd == 8:
        return True
    return False

def extraer_digito(dni):
    dni1 = str(dni)
    id = dni1[0] + dni1[1] + dni1[2]
    return id

nombre1 = str(input('Escriba su primer nombre: '))
while nombre1!= '':
    nombre2 = str(input('Escriba su segundo nombre: '))
    apellido1 = str(input('Escriba su apellido: '))
    dni1 = int(input('Digite su DNI: '))
    while valido_dni(dni1) == False:
        dni1 = int(input('Digite su DNI: '))
            
    print('-' * 50)
    print(f'Apellido: {apellido1} ')
    print(f'Nombre: {nombre1}')
    print(f'DNI: {dni1}' )
    idSoc = nombre1 + str(len(apellido1))+ extraer_digito(dni1)
    print(f'ID socio: {idSoc} ')
    nombre1 = str(input('Escriba su primer nombre: '))
    
