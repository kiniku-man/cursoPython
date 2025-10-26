'''
Write a program that prompts to enter a string of text.

    The program should print the original text followed on a second line in the output by the number of characters entered.
'''

dato=input("Indica un texto:")
longitud=len(dato)
print(dato)
# print("Contiene: " + longitud + " caracteres")    # Para usar esta hay que convertir a texto la variable longitud -> longitud=str(longitud)   
print("Contiene {numero} de caracteres.".format(numero=longitud))