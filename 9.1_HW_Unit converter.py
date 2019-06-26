# Exercise 9.1: Unit converter

km_int = 0
mi_int = 0

print("Greeting, ")
print("This program is a converter from kilometers to miles ...")

while True:
    km_int = input("Please enter kilometers: ")

    mi_int = int(km_int) * 0.62

    print("The result is: " + str(mi_int))

    another = input("Want you to repeat? (y,n): ")

    if another != "y":
        break
