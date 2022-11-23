print('Calculadora de riego')

temp = float(input('Escriba la temperatura: '))
agua_p = float(input('Cantidad de agua para el platin: '))

if temp < 10:
    riego = agua_p + 0
elif temp <= 20:
    riego = agua_p + 5
elif temp <= 25:
    riego = agua_p + 10
else:
    riego = agua_p + 20

print(f'El platin necesita para la temperatura {temp} un riego de {riego}mm3')

