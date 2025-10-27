'''
Use a range to loop through and print each number from 0 to 49 to produce the following output.

    Each number should be printed individually as opposed to concatenating them as a string.

 0  1  2  3  4  5  6  7  8  9
10 11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47 48 49
'''
valor=0
for i in range(0,5):
    print()
    for j in range(0,10,1):
        if valor < 10:
            print("",end=" ")
        print(valor,end=" ")
        valor=valor+1