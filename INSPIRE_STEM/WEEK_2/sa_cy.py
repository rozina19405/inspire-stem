#program to calculate surface area of a cylinder
# Date : 20/02/2024
# Name : Rozina Adhiambo

import math

r = float(input ("Enter the radius of the cylinder:" ))
h = float(input ( "Enter the height of the cylinder : " ))

sa= (2 * math.pi * r * h )+( 2 * math.pi * r ** 2)

print (" The surface area of the cylinder is : " , sa )
