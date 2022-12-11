# Project to make a Random Password generator

from random import *
import array
 
def gen(max): #Password generator function
    
#All valid inputs
    d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm',
          'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
 
    uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M',
          'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
 
    s = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~','*', '(', ')']
 
    Combine = d + uc + lc + s
 

    ran_digit = choice(d)
    ran_upper = choice(uc)
    ran_lower = choice(lc)
    ran_symbol = choice(s)
 
    temp_pass = ran_digit + ran_upper + ran_lower + ran_symbol
 
 

    for x in range(max - 4):
        temp_pass = temp_pass + choice(Combine)
 
#Shuffle list
        temp_pass_list = array.array('u',temp_pass)
        shuffle(temp_pass_list)
 
    password = ""
    for x in temp_pass_list:
            password = password + x
    return password


while(True):
    response=int(input("""\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Welcome To Password Generator !\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    \nPress 0 to Exit
    \nPress 1 to generate Password
    \nEnter your response as per above menu: """))
    if(response==1):
        len=int(input("Please enter the password length: "))
        if(len>=12):
            print("\n\nThe random password is: %s\n\n"%(gen(len)))      
        elif(len<12):
            print("\n\nPlease enter a length more than or equal to 12 and a positive number\n\n")
        else:
            print("Error Please enter a correct value\n\n")
    elif(response==0):
        print("\nExited Succesfully")
        break
    else:
        print("\nInvalid Input\n\n")
