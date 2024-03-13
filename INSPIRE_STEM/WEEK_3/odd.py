# this is a program to output odd numbers between 0- 20
# date : 29/02/2024
# name : Rozina Adhiambo

def print_odds(first_num , last_num):
    for i in range (first_num,last_num):
        if i % 2 : 
            print (i)

print_odds (0,16)