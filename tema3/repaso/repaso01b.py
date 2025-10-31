''' 
Escribe un programa que calcule la suma de todos los elementos de una lista de números.
'''

def suma(lista):
    total=0
    
    for i in lista:
        total=total+i
    
    return(total)


numeros=[1,2,3,4,5,6]

resultado=suma(numeros)
print("La suma total es {sumaTotal}".format(sumaTotal=resultado))
