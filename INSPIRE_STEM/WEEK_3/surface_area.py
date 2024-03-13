# this is a program to  calculate sa of solids
#date 29/02/2024
# name: Rozina Adhiambo

import math

shape = str(input("Enter the type of solid: "))

if shape ==("cylinder"):
    r = float(input("enter radius: "))
    h = float(input("enter height: "))

    def sa_cyl(r,h):
        return ((math.pi * 2* r *h) + (2 *math.pi * r **2))
    print (sa_cyl(r,h))

elif shape == ("cube"):
    s = float(input("enter the length of one side: "))

    def sa_cube(s):
        return((s**2)*6)
    print(sa_cube(s))

elif shape == ("sphere"):
    r = float(input("enter the radius: "))

    def sa_sphere(r):
        return(4*math.pi* r**2)
    print(sa_sphere(r))

else: 
    r = float(input("enter the radius: "))
    l = float(input("enter the slant length of the side: "))

    def sa_cone(r,l):
        return ((math.pi * r* l)+ (math.pi * r **2))
    print(sa_cone(r,l))

