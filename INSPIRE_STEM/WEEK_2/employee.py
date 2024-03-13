# this is a program to handle eployee funds
# date : 21/02/2024
# name : Rozina Adhiambo

e_name = input("Enter the employee's full name : " )
e_age = input (" Enter the employee's age : " )
e_salary = float(input (" Enter the employee's salary : "))
e_bonus = float(input (" Enter the employee's bonus : "))

e_earnings = e_salary + e_bonus

print("")
print (" The employee's full name is : " , e_name)
print (" The employee's age is : " , e_age)
print (" The employee's salary is : " , e_salary)
print (" The employee's bonus is : " , e_bonus)
print (" The employee's total earnings are : " , e_earnings)
print ("")
print("After Changes.")

e_salary = e_salary * 1.3
e_bonus = e_bonus - 5000

e_earnings = e_salary + e_bonus

print("")
print (" The employee's full name is : " , e_name)
print (" The employee's age is : " , e_age)
print (" The employee's salary is : " , e_salary)
print (" The employee's bonus is : " , e_bonus)
print (" The employee's total earnings are : " , e_earnings)

