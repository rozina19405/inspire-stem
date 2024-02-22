# this is a program to display the pascal's triangle
# date : 23/02/2024
# name : Rozina Adhiambo

from math import factorial

rows = int(input ("Enter pascals triangle number pattern rows: "))

print ("PASCAL'S TRIANGLE")

for n in range (0, rows):
    for j in range(rows -n +1):
        print(end = " ")
    for k in range (0, n+1):
        print (factorial (n)// (factorial(k)*factorial (n-k)), end = " ")
    print()
    
        