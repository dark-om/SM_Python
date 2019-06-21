#Homework 7.3: Calculator

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operation_num = input("Enter operation (+,-,/,*): ")
print("Calculation is: ")

if operation_num == "+":
    print(first_num + second_num)
elif operation_num == "-":
    print(first_num - second_num)
elif operation_num == "/":
    print(first_num / second_num)
elif operation_num == "*":
    print(first_num * second_num)
else:
    print("Wrong operator input.")