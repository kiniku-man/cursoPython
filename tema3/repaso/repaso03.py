'''
    Escribe un programa que elimine los elementos duplicados de una lista y muestre la lista resultante.
'''

numeros=[1,1,2,3,4,4,5,5,6] # Lista original con duplicados

sinDuplicados=list()    # Lista final sin duplicados

for i in numeros:
    if not i in sinDuplicados:
        sinDuplicados.append(i)

print("La lista con duplicados es: {numeros}".format(numeros=numeros))

print("La lista sin duplicados es: {sinDuplicados}".format(sinDuplicados=sinDuplicados))