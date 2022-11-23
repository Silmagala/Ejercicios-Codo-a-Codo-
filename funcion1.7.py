def crear_lista(numero, cant_palabra):
    lista_pal = []
    for y in range(numero):
        lista_pal.append([])    
        for x in range(cant_palabra):
            lista_pal[y].append(x) = str(input('Introduzca palabra: '))
    return lista_pal

l1=[],[]
print('Generador de listas')
cant_lista = int(input('¿Cuantas listas quieres escribir?: '))
for x in range(1, cant_lista + 1):
    numero = int(input(f'Digite cuantas palabras tiene la lista {x}: '))
    while numero < 1:
        numero = int(input('Digite cuantas palabras tiene la lista: '))
for x in range(cant_lista + 1):
    print(f'La lista {x} es: {crear_lista(cant_lista, numero)}')
