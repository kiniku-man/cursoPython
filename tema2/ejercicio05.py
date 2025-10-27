'''
Ask the user to input multiple numbers on one input line.

    Split the numbers into a list.

    Write a loop that examines each element of the list and displays the ones that are greater than zero.
'''
numeros=input("Indica los números: ")
lista=numeros.split()
print(lista)
for i in lista:
    if int(i) >= 0:
        print(i)

