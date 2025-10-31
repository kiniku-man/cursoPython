'''
    Crea un programa que invierta el orden de los elementos de una lista.
'''

numeros=[1,2,3,4,5,6]   # Lista de números

alreves=list()  # Lista donde almacenar el resultado inverso

for i in numeros:
    alreves.insert(0,i) # Insertamos el elementos en la primera posición de la lista

print(alreves)  # Mostramos el resultado. Lista inversa

