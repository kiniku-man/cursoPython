'''
Rewrite the preceding exercise to additionally print out 
how many digits are in the number, if the number is an integer.
'''

resp=input("Indique un valor: ")

if not resp.isnumeric():
    print("Introdujo un valor que no es numérico.")
else:
    x=len(resp)
    print("El número tiene {x} dígitos".format(x=x))

