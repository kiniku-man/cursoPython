'''
Given the following two lists:

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

    Concatenate the two lists by index into a new list that, when printed, looks as follows:

["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
'''

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]   # Primera lista
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]  # Segunda lista

listaFinal=list()

long=len(first)

for i in range(0,long):
    print(first[i] + ", " + second[i])
    # p1=first[i]
    # p2=second[i]
    # dato=p1+p2
    listaFinal.append(first[i]+second[i])
print(listaFinal)