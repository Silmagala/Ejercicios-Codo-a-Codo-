#Determinar si una direccion es valida o no
def main(correo):
    for x in correo:
        if x == '@':
           return True
    return False

correo1 = input('Escriba su correo')

if main(correo1):
    print('Su correo es correcto')
else:
    print('Correo incorrecto')


