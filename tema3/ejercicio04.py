'''
Use a single set to determine the number of unique words in the user's input.

    You can use the same sample while loop from Exercise 1.

        Each time through the loop, the individual words should be added to the single set.

    When done looping, output the contents of the set sorted alphabetically.

    Also, output the number of unique words.
'''

texto=input("Indique su texto: ")
lista=set()
x=0

for i in texto:
    if not i in lista:
        lista.add(i)
        x=x+1
print(lista)            # Lista sin ordenar
print(sorted(lista))    # Lista ordenada
print(x)                # Número de números