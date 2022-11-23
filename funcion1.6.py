def crear_lista(cant_palabra):
    lista_pal = []
    for x in range(cant_palabra):
        palabras = str(input('Introduzca palabra: '))
        lista_pal.append(palabras)
    return lista_pal

numero = int(input('Digite cuantas palabras tiene la lista: '))
while numero < 1:
    numero = int(input('Digite cuantas palabras tiene la lista: '))
print(f'La lista creada de palabras es: {crear_lista(numero)}')

