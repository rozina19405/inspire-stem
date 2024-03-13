# this is a program to calculate a term in a geometric prograssion
# date : 20/02/2024
# name : Rozina Adhiambo

a = float(input("Enter the first term of the sequence : " ))
r = float(input (" Enter the common ratio : "))
n = float(input (" Enter the number of terms in the sequence"))

nth = a * ( r ** (n - 1) )

print ("The nth term of the sequence is :" , nth)
