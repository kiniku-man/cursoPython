'''
    Desarrolla un programa que cuente cuántos números pares hay en una lista de enteros.
'''

numeros=[1,2,3,4,5,6]   # Lista de valores

pares=0 # Conteo de números pares

for i in numeros:
    if i%2==0:
        pares=pares+1

print ("El número total de números pares es: {pares}".format(pares=pares))