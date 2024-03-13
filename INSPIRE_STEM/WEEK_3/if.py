# executes a statememnt only if a condition is true
# this program uses if else
# date : 25/02/2024
# name : rozina adhiambo

age = 17
if age > 18 :
    print ("You are allowed to drive.")
#using and
salary = 45000
if salary < 50000 and salary > 30000 :
    print ( salary * 0.1 + salary)

salary =int(input("Enter the salary:" ))
if salary < 50000 and salary > 30000 :
    print ( salary * 1.1)

#using or
home_county = "Nyeri"
if home_county == "Nyeri" or home_county == "Kisii":
    print ("You get a bursary.")

# using if else
grade = 70

if grade >= 84 and grade <= 90:
    print (" You are win a calculator")
elif grade >= 50 and grade <= 83 :
    print ("You win a mathematical set")
else:
    print ("You get nothing!")
