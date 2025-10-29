'''
Rewrite Exercise 4 to count the frequency of each word in the user's input.

    A dict provides the perfect data structure for this problem.

        Let the words be the keys, and let the counts be the values.

    Print the results sorted by the words.

    Finally, print the results sorted by the counts.
'''

dato=input("Indique frase: ")
lista=dict()    # Creamos un diccionario vacío
for i in dato:
    chivato=0
    for x,y in lista.items():
        if x == i:              # Si se encuentra la letra en el diccionario se marca chivato para no guardarla
            chivato=1           # y se incrementa su valor.
            y=y+1
            lista[i]=y
    if chivato == 1:
        chivato=0
    else:
        lista[i]=1
print(lista)