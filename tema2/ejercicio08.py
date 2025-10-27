'''
Rewrite exercise # 4 such that the program takes into account the case where the first number 
entered is bigger than the last.

    For example, if the user inputs the numbers 10 and 15, then the sum would be 75.

10 + 11 + 12 + 13 + 14 + 15 = 75

    If the user inputs the numbers 15 and 10, then the sum would be still be 75.
'''

num1=int(input("Indique un número: "))
num2=int(input ("Indique un número: "))

if num1<num2:
    low=num1
    high=num2
else:
    low=num2
    high=num1

x=0
for i in range(low,high+1):
    x=x+i
print("La suma total es {x}".format(x=x))