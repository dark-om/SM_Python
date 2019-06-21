#Homework 7.1: The mood checker

input_mood = input("Your mood: ")

if input_mood == "happy":
    print("It is great to see you happy!")
elif input_mood == "nervous":
    print("Take a deep breath 3 times.")
elif input_mood == "sad":
    print("Take a deep breath 5 times.")
elif input_mood == "excited":
    print(":-)")
elif input_mood == "relaxed":
    print("Cool!")
else:
    print("I don't recognize this mood")