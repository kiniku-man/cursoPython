def mi_funcion():
    print("HolaMundo")

def mi_funcion2(texto):
    print(texto)

def mi_funcion3(texto):
    return 4

def volume(length, width, height):
    """Returns the volume of a box for given dimensions"""
    return length * width * height

def volume2(length=10, width=5, height=2):
    """Returns the volume of a box for given dimensions"""
    return length * width * height

def the_sum(*args):
    total = 0
    print("Parameter type:", type(args), end=" ")
    for elem in args:
        total += elem
    return total


mi_funcion()
mi_funcion()
mi_funcion()

mi_funcion2("prueba")

valor=mi_funcion3("tres")
print(valor)

dim1 = float(input("Enter length of the box: "))
dim2 = float(input("Enter width of the box: "))
dim3 = float(input("Enter height of the box: "))
result = volume(length=dim1, width=dim2, height=dim3)
print("The volume is:", result)

print("3:", volume2(2))




total = the_sum(1, 2, 3, 4, 5)
print(total)
