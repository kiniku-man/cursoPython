# Comentario

print ("Hola Mundo")

length=10;ancho=40 # Sensitive case, ¡cuidado!.
area=length*ancho
print(area)

mensaje= "Este mensaje ocupará más de una linea por ello \
escribimos de esta manera la multimlínea."
print(mensaje)

resultado= 500 * 3 + \
4 + 7

print(resultado)

print("Este mensaje también se puede" \
"cortar por la mitad porque está entre paréntesis") # El paréntesis no es necesario al usar paréntesis

print("Este mensaje también se puede",
"cortar por la mitad porque está entre paréntesis")

print("a", "b", "c")

print("a", "b", "c", sep=',')

input("Introduce un número:")    # Siempre devuelve un string

nom=input("Introduce tu nombre:")
print("Hola ", nom)

# Python reconoce números enteros, float y complejos. Scalar types
# 

print (17/5)
x=17//5
print (x)
x=17%5
print (x)

print (2**3)

x = " Esta cadena de \
texto tiene varias \
líneas."

print (x)

x= """Esta cadena
de texto
mantiene los saltos"""

print(x)

x="Prueba"
print(x[2])
print(x[2:5])

nombre = "Sergio"
Apellido="Ortiz"
Fecha="lunes 4 de septiembre"

print("Hola " + nombre + " " + Apellido + ", la entrega se hará el " + Fecha + ".")

print("Hola {0} {1}, la entrega se hará el {2}".format(nombre, Apellido, Fecha))

print("Hola {nombre} {apellido}, la entrega se hará el {fecha}".format(nombre=nombre, apellido=Apellido, fecha=Fecha))

print(f"Hola {nombre}")