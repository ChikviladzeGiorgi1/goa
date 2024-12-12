number = int(input("enter your number: "))
sum_number = 0
for i in range(number + 1):
    sum_number += i

print("diapazoni aris", sum_number)

correct_password = "paroli"
counter = 0
password_correct = False
while not password_correct:
    user_password = input("enter your password: ")
    counter += 1
    if user_password == correct_password:
        correct_password = True
        print("accses grainted")
        print(f"the password has been enterd {counter}")
    else:
        print("password is incorrect")
        
import random

num = random.randint(1, 10)
counter = 0
correct_guess = False
while not correct_guess:
    user_guess = int(input("enter your name ( 1-10 ) " ))
    counter += 1
    if user_guess == num:
        print(f"You guessed the correct number! It was {num}.")
        print(f"You took {counter} attempts to guess the number.")
        correct_guess = True
    else:
        print("incorrect. try again")    

                          

