# this is a program to calculate the sum of the first 20 numbers using for loops
# date : 26/02/2024
# name : Rozina Adhiambo

sum_nums = 0
max_val = int(input("Enter the maximum number: "))
for x in range(0,max_val + 1 ):
    sum_nums = sum_nums + x
    print (sum_nums)
