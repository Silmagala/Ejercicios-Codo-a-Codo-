productoAelaborar = int(input('''
¿Qué producto deseas elaborar?
1.-ProductoA
2.-ProductoB
'''))
if productoAelaborar > 0 and productoAelaborar < 3:
    cant_A_elaborar = int(input('¿Qué cantidad deseas elaborar?'))

    if productoAelaborar == 1:
        cant_mate_A = cant_A_elaborar * 20
        cant_mate_B = cant_A_elaborar * 10
        cant_mate_C = cant_A_elaborar * 3
    elif productoAelaborar == 2:
        cant_mate_A = cant_A_elaborar * 5
        cant_mate_B = cant_A_elaborar * 2
        cant_mate_C = cant_A_elaborar * 10


    print('*****************************************')
    print( 'INFORME DE PRE PROCUCCIÓN')
    print('*****************************************')
    print(f'''Producto a elaborar: {productoAelaborar}
    Cantidad a elaborar: {cant_A_elaborar}
    Materias primas necesarias:
    - materia prima A: {cant_mate_A}
    - materia prima B: {cant_mate_B}
    - materia prima C: {cant_mate_C}''')
    print('*****************************************')
else:
    print('Error, codigo del producto a elaborar.')