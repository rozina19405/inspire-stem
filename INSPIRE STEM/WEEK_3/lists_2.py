# creating a list of friends
#date
#name

friends = ["Kelsey", "Angie", "Nduku","Tim", "Anto", "joyanne", "ruth"]
# iterating the list
for friend in friends :
    print (friend)

# to copy one list into another
enemies = friends [:]
print(enemies)

# to slice the list (to get part of a list)
fruits = ["pineapple", "orange","mango","apple","watermelon"]

print (fruits[0:3])# prints the first 3 items in the list

#deleting elements in a list

del fruits[0]
print (fruits)

squares = []# initializes an empty list

for x in range (0,11):
    squares.append (x**2)
print(squares)
