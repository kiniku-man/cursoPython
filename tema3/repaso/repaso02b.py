'''
Crea un programa que encuentre y muestre el número más grande en una lista.
'''

def mayor(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
    return(mayor)

numeros=[1,2,3,6,5,4]

resultado=mayor(numeros)
print(resultado)