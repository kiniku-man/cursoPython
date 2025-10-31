''' 
Escribe un programa que calcule la suma de todos los elementos de una lista de números.
'''
numeros=[1,2,3,4,5,6]   # Declaración de la lista que usaremos.

total=0 # Variable donde almacenaremos la suma total de los números

for i in numeros:
    total=total+i

print("La suma tota es {total}".format(total=total))

