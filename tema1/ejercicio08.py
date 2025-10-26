'''
Write a program that prompts the user twice for a number.

    The first number will be the base, and the second number will be the exponent.

        Print the result of raising the base to the exponent.
'''
num1=int(input("Indique el primer número: "))
num2=int(input("Indique el segundo número: "))
resultado=num1 ** num2
print(resultado)