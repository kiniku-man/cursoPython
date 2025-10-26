'''
Write a program that prompts twice for text from the user.

    The first input should be a first name.

    The second input should be a last name.

    The program should print the full name on one line and the person's initials on the second line.
'''

nombre=input("Indique su nombre: ")
apellido=input("Indique su apellido: ")
fn=nombre[0]
fa=apellido[0]
print(nombre + " " + apellido)
print("{nombre} {apellido}".format(nombre=nombre, apellido=apellido))
print(fn + " " + fa)