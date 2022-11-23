def es_bisiesto(anio):
    if anio % 400 == 0 or anio % 100 != 0 and anio % 4 == 0:
        return True
    else:
        return False


dig_anio = int(input('Digite el año AAAA: '))

if es_bisiesto(dig_anio):
    print(f'Es bisiesto {dig_anio}')
else:
    print(f'No es bisiesto {dig_anio}')
