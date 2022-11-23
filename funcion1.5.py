def es_bisiesto(anio):
    if anio % 400 == 0 or anio % 100 != 0 and anio % 4 == 0:
        return True
    else:
        return False


dig_anio1 = int(input('Escriba un año: '))
dig_anio2 = int(input(f'Escriba otro año posterior a {dig_anio1}: '))

contador = 0
contadorB = 0
aaaa = dig_anio1 
while dig_anio2 < dig_anio1:
    if dig_anio2 < dig_anio1:
        dig_anio2 = int(input(f'{dig_anio2} no es mayor que {dig_anio1} intentelo de nuevo: '))
    while aaaa <= dig_anio2:
        if es_bisiesto(aaaa):
            contadorB += 1
        contador +=1
        aaaa += 1
print(f'De: {dig_anio1} a {dig_anio2} hay {contador}, {contadorB} de ellos bisiestos ')
