'''
Write a program that asks the user to enter a sentence.

    The program should determine and print the following information:

        The first character in the string of text and the number of times it occurs in the string.

        The last character in the string of text and the number of times it occurs in the string.
'''
dato=input("Indique una frase: ")
pc=dato[0]

# print("El primer caracter es " + pc + " y aparece " + dato.count(pc) + " veces")
print("El primerar caracter es {pc} y se repite {veces}".format(pc=pc,veces=dato.count(pc)))

x=len(dato)-1
uc=dato[x]
print("El primerar caracter es {uc} y se repite {veces}".format(uc=uc,veces=dato.count(uc)))
