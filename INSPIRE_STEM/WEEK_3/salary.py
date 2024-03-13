# this is a program to manipulate employees' salaries
# date : 26/02/2024
# name : Rozina Adhiambo

e_salary = float(input("enter the employee's salary : "))

if e_salary < 100000:
    e_salary= e_salary * 0.3 + e_salary
    print("the new salary is :" ,e_salary)
elif e_salary<= 150000 :
    e_salary= e_salary * 0.15 + e_salary
    print("the new salary is :" ,e_salary)
elif e_salary > 150000 :
    e_salary= e_salary * 0.05 + e_salary
    print("the new salary is :" ,e_salary)
