# this is a program to demonstrate loops.
# date : 27/02/2024
# name : Rozina Adhiambo

movies= ["human centipede", "the menu", "vivarium", "chucky", "the little mermaid"]
print (movies)

for _ in range(2):
    movies.pop(0)
    print ("\n")
    print(movies)

movies.sort()
print("\n")
print(movies)

movies.reverse()
print("\n")
print(movies)

print("\n")
total_movies = len(movies)
print("The total number of movies available is: " , total_movies)