'''
Ask the user to input three numbers representing a lower limit, a higher limit, and a step value.

    The program should use a range object to loop through and print the numbers from low 
    to high (inclusive), taking into consideration the step.
'''
low=int(input("Indique el valor bajo: "))
high=int(input("Indique el valor alto: "))
step=int(input("Indique el step: "))

for i in range(low,high,step):
    print(i)