'''
    Determine and print the following information about the string:

        Does it end in a period?

        Does it contain all alphabetic characters?

        Is there an 'x' in the string?

    Create and print a new string that has all occurrences of e changed to E.
'''

dato=input("Indique un texto: ")
print("El dato introducido es: " + dato)
print(dato.endswith("."))   # No = Flase, Sí = True
print(dato.isalpha())
print(dato.find('x'))
print('x' in dato)
modificada=dato.replace('e','E')
print(modificada)


