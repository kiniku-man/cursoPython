'''
Write a program that creates a loop asking the user to input a number.

    Repeat this process until the user enters the value end.

    Enter each number into a set.

        Before you enter the number, verify if the number is already in the set.

        If the number is already in the set, then update a counter that tracks how many entries are 
        not added to the set.

    Just before the program ends, print the following:

        The contents of the set on one line

        The number of elements that were NOT added to the set on the second line
'''

lista=set()
texto=("Introduzca el dato o end para salir: ")
x=0 # Contador de veces que no añadimos dato al set
while True:
    dato=input(texto)
    if not dato in lista and dato != "end":
        lista.add(dato)
    elif dato == "end":
        break
    else:
        x=x+1

print(lista)
print(x)