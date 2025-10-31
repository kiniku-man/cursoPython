'''
Crea un programa que encuentre y muestre el número más grande en una lista.
'''

numeros=[1,2,3,6,5,4]

mayor=0

for i in numeros:
    if i > mayor:
        mayor=i

print("El número mayor es {mayor}".format(mayor=mayor))

