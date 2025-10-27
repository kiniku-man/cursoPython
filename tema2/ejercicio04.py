'''
Write a program that prompts twice for an integer.

    The program should output the sum of the integers within the range of those two numbers inclusively.

    For example, if the user inputs the numbers 10 and 15, then the sum would be 75.

10 + 11 + 12 + 13 + 14 + 15 = 75

'''
num1=int(input("Indique el primer número: "))
num2=int(input("Indique el segundo número: "))

x=0
for i in range(num1,num2+1):
    x=x+i
print("La suma total es {x}".format(x=x))
