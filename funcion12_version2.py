def strc(texto):
        fin = len(texto)
        print(fin)
        # Llegar a la última posición de la última letra
        while fin > 0 and texto[fin - 1] == ' ':
            print(texto[fin - 1])
            fin -= 1

        inicio = fin
                 #Obtener la posición de la primera letra de la última palabra
        while inicio > 0 and texto[inicio - 1] != ' ':
             inicio -= 1
        L=fin - inicio
    
        return L,texto[inicio:fin]
 
texto = str(input('Frase: '))
print(strc(texto))

