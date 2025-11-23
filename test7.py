 
import random

number_of_attempts = 5

while True:

    user_num = int(input("Enter a number between 1 and 10: "))
    x = random.randint(1, 10)
    
    if user_num == x:
        print("You win!")
    else:
        print(f"You lose! The number was {x}")
    
    if input("Again? (y/n): ").upper() == "N":
        break