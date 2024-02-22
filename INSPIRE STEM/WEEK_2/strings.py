# strings in python
# Date: 22/02/2024
# Name : Rozina Adhiambo

city = "Nairobi"
# printing individual characters in a string
print (city [0]) # prints N
print (city [1]) # prints a
print (city [2]) # prints i
print (city [3]) # prints r
print (city [4]) # prints o
print (city [-1]) # prints i
# print (city [8]) # prints out of range
print (city [-2]) # prints b
print (city [-3]) # prints o

# converting to uppercase
print (city)
print("\n") # prints a new line
print (city.upper())
#converting to lowercase
name = "ROZINA ADHIAMBO"
print("\n")
print (name)
print ("\n")
print (name.lower()) 

town = "          Naivasha            "
print (town)
print ("\t")#prints a new tab
print(town.strip())

# adding two strings (concatenation)

f_name = "Rozina"
s_name = " Adhiambo"

full_name = f_name + s_name
print ("\n")
print (full_name)

# replacing a character 

fruit = "Orange"
print (fruit)
print (fruit.replace ("O", 'Y'))
print ("\n")
fruit = "OrangeOOOO"
print (fruit)
print (fruit.replace ("O", 'Y'))

# spliting strings

subject = "Physical,Sciences"

print (subject.split(","))
print("\n")
subject = "Physical:Sciences"

print (subject.split(":"))
print("\n")

# formatting strings 

age = 18
height = 1.2
print ("I am {} years old ." .format (age) )

print ("I am {0} years old and {1} meters tall." .format (age, height) )

 # when there are many strings to be formatted, index them starting with 0
