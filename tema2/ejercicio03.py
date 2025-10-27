'''
Write a program that prompts twice for an integer.

    The program should print the larger of the two numbers.

    If the numbers are equal, then the program should indicate it as such.
'''

num1=int(input("Indique un número: "))
num2=int(input("Indique un número: "))

if num1 > num2:
    print("El {num1} es mayor que el {num2}".format(num1=num1,num2=num2))
elif num1 < num2:
    print("El {num1} es menor que el {num2}".format(num1=num1,num2=num2))
else:
    print ("Son iguales")

