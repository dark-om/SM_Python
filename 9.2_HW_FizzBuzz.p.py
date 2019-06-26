# Homework 9.2: FizzBuzz

int_numb = int(input("Select a number between 1 and 100: "))
print(int_numb)

for calc in range(1, int_numb+1):
    if calc % 3 == 0 and calc % 5 == 0:
        print("fizzbuzz")
    elif calc % 3 == 0:
        print("fizz")
    elif calc % 5 == 0:
        print("buzz")
    else:
        print(calc)