#program to solve the quadratic equation
# Date : 20/02/2024
# Name : Rozina Adhiambo

import math 

a = float(input(" Enter the coefficient of first term : "))
b = float(input(" Enter the coefficient of second term : "))
c = float(input(" Enter the constant: "))

d =(b ** 2) - 4 * a * c

x_1 =( -b + math.sqrt(d) )/ 2 * a
x_2 =( -b - math.sqrt(d) )/ 2 * a

print ( " the first solution of the quadratic equation is", x_1)
print ( " the second solution of the quadratic equation is", x_2)