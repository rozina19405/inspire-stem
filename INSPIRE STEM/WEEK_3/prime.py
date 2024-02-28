# this is a program to print prime numbers between  0 and 20
# date 26/02/2024
# name : Rozina Adhiambo

for num in range (0,21):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else: print(num)