#program to calculate higher purchase price
# Date : 20/02/2024
# Name : Rozina Adhiambo


dep = float(input ("Enter the deposited amount :" ))
n = float(input("Enter the number of months : " ))
inst = float(input ("Enter the monthly installment paid : "))

hpp = dep + ( n * inst )

print( " The higher purchase price is : ", hpp)
