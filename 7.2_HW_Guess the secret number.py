#Homework 7.2: Guess the secret number

var_secret = 5

input_guess = input("Guess the secret number:")

var_guess = int(input_guess)

if var_guess == var_secret:
    print("GREAT!!!!")
else:
    print("Unfortunately, the wrong answer...")