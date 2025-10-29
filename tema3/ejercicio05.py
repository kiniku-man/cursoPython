'''
Use a dictionary to create a mapping from the digits 0-9 to the words zero, one, two, etc.

    Next, ask the user to input a number.

    If the user enters 1437, then the program should print one four three seven. 
'''

lista={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

entrada=int(input("Introduzca un número del 0 al 9: "))
valor=lista['0']
print(valor)