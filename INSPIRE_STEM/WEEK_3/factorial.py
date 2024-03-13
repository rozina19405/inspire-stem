# this is a program to calculate factorials of numbers
# date : 25/02/2024
# name : Rozina Adhiambo

factorial_nums = 1
max_val = int(input("Enter the maximum number: "))
for x in range(1,max_val + 1 ):
    factorial_nums = factorial_nums * x
    print (factorial_nums)

