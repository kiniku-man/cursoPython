'''
    Escribe un programa que calcule el promedio de los elementos de una lista de números.
'''

numeros=[12,23,45,100]

cantidad=len(numeros)

suma=0

for i in numeros:
    suma=suma+i

resultado=suma/cantidad

print(resultado)

