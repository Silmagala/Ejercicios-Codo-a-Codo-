#Logica del programa
metros_cuadrado = float(input('Cantidad de metros cuadrados sobre el que se calculara el presupuesto: '))

costo_ladrillos = float(input('Costo de metro cuadrado ladrillo: '))
costo_cemento   = float(input('Costo de metro cuadrado cemento: '))
costo_arena     = float(input('Costo de metro cuadrado arena: '))

total_ladrillos = metros_cuadrado * costo_ladrillos
total_cemento   = metros_cuadrado * costo_cemento
total_arena     = metros_cuadrado * costo_arena

importe_total = total_ladrillos + total_cemento + total_arena

#Inicio del programa
print()
print('*' * 28)
print('Presupuesto de mantenimiento')
print('*' * 28)

print(f'Metros cuadrados: {metros_cuadrado}')
print()
#------------------------------------------------------
print('Precio de materiales por metros cuadrados')
print(f'-Ladrillos: ${costo_ladrillos}')
print(f'-cemento  : ${costo_cemento}')
print(f'-Arena    : ${costo_arena}')
print()
#------------------------------------------------------
print('Costo total de materiales:')
print(f'Total de ladrillos: ${total_ladrillos}')
print(f'Total de cemento  : ${total_cemento}')
print(f'Total de arena    : ${total_arena}')
print()
#------------------------------------------------------
print(f'Importe total de la obra:${importe_total}')


