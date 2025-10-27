'''
Write a program that prompts for a lucky number. 
The program should print out a message if the number entered is not an integer.
'''

resp=input("Indique un valor: ")

if not resp.isnumeric():
    print("Introdujo un valor que no es numérico.")