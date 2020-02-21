import random

print("Welcome to the Guessing Number Game!!!!!!")    
random_num = random.randrange(0, 100)
chance = 0
while True:
    user_input = int(input("Enter a number between 0 to 99: "))
    if user_input in range(100):
        if user_input == random_num:
            print("You Win :)")
            exit(0)
        else:
            print("Try again!!!!!!")
    else:
        print("Enter a correct number!!!!!")
    chance += 1

    if chance >= 3:
        if user_input < random_num:
            print(f"{user_input} is lower the winning number")
        elif user_input > random_num:
            print(f"{user_input} is higher the winning number")