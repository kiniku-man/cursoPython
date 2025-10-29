'''
Given the following two lists:

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

    Concatenate the two lists by index into a new list that, when printed, looks as follows:

["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
'''

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

x=len(first)
listaFinal=list()

for i in range(0,x):
    datos=first[i]+second[i]
    listaFinal.append(datos)

print(listaFinal)