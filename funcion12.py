""" def long_ult_palabra(texto, res):
    palabras = texto.split()
    for x in palabras:
        print (x.strip())
    

test_string = str(input('Introduce frase: '))
  
print("El texto original es : " + test_string) 
  
res = len(test_string.split()) 
   
print("El numero de caracteres de la ultima palabra es : ", long_ult_palabra(test_string))  """

class Solution:
    def strc(self, s):
        end = len(s)
        # Llegar a la última posición de la última letra
        while end > 0 and s[end - 1] == ' ':
            end -= 1
        
        start = end
                 #Obtener la posición de la primera letra de la última palabra
        while start > 0 and s[start - 1] != ' ':
             start -= 1
        L=end - start
    
        return L,s[start:end]
 
s = Solution()
print(s.strc(' Amo el amor de los marineros'))


