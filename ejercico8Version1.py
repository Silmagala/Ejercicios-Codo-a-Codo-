especies = [
    ['Tomate', 43.7],
    ['Pimiento',30.5],
    ['Pepino', 52.0],
    ['Chicharo', 5.9],
    ['Albahaca', 0.63]
]
proceso = 'S'
print('Calculadora de riego')
temp = float(input('Escriba la temperatura: '))
print('***************************************')
while proceso.upper() == 'S':
    for x in especies:
        if temp < 10:
            riego = x[1] + 0
        elif temp <= 20:
            riego = x[1] + 5
        elif temp <= 25:
            riego = x[1] + 10
        else:
            riego = x[1] + 20
        print(f'{x[0]} necesita para la temperatura {temp} un riego de {riego}mm3')
    proceso = input('¿Deseas repetir el proceso?S/N' )
    print()

