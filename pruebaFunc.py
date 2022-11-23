correo = input("Digite la direccion de correo electronico: ")
valido = False
contadorArroba = 0
contadorPunto = 0

for i in correo:
  if(i == '@'):
    contadorArroba += 1
    valido = True
  if(contadorArroba != 1 and contadorPunto < 1):
     valido = False
  if(i == '.'):
    contadorPunto += 1

print(contadorArroba)
print(valido)

if(valido):
   print("el Correro: "+ correo+" es correcto")
else:
   print("direccion erronea")