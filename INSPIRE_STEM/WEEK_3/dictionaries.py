#dictionaries
# date : 28/02/2024
#name : Rozina Adhiambo

my_laptop = {"make":"HP","colour": "Black","weight": "1.2",
             "year":"2024"}

# to print items in the dictionary
'''
for key,value in my_laptop.items():
    print(key)
    print (value)
    print("\n")
'''
    
# to print individual items in the dictionary

print(my_laptop["make"])
print(my_laptop["colour"])
print(my_laptop["year"])

# tochange values in a dictionary
my_laptop ["colour"] = "red"
my_laptop ["year"] = "2009"
print(my_laptop)

my_laptop["size"]= "1200mm x 600mm"
print (my_laptop)

# deleting elements in a dictionary

del my_laptop["colour"]
print (my_laptop)

# copying

siz_laptop = my_laptop.copy()
print(siz_laptop)