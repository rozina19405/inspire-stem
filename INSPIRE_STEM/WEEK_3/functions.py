# this is a program to use functions
# date : 29/02/2024
# name : Rozina Adhiambo

# how to define a function

def print_name(): 
    print("My name is Rozina Adhiambo.") # this is the function definition

# calling the function

print_name()
print_name()
print_name()

# creating a function that prints my details
# it has parameters

def print_details(name,age,id,gender):
    print("I am {0}. i am {1} years old . my id number is {2}. my gender is {3}".format(name,age,id,gender) )

# calling the function
print_details("Rozina Adhiambo","18","8974564","female")
print_details("Joyanne Shekinah","18","8456890","female")

# creating another function to sum numbers

def sum_nums (x,y):
    return x + y

z = sum_nums (10,20)

print(z)

# creating another function to multiplynumbers

def prod_nums (x,y):
    return x*y

print(prod_nums(5,16)) # you dont have to assign it another variable

# crating a function that prints odd numbers from 1 to 10

def print_odds(first_num , last_num):
    for i in range (first_num,last_num):
        print(i%2)

print_odds (0,15)

