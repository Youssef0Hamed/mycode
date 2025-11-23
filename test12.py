import random
import time
choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("\nRock Paper Scissors Game\n1) Rock\n2) Paper\n3) Scissors\nQ) Quit\n> ")

    if user_choice == "q":
        print("Thanks for playing! 👋")
        break

    if user_choice not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1, 2, 3, or Q.")
        continue

    user_move = choices[int(user_choice) -1]
    computer_move = random.choice(choices)

    print(f"\nYou chose: {user_move}")
    print(f"Computer chose: {computer_move}")

    if user_move == computer_move:
        time.sleep(1)
        print("It's a tie!")
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        time.sleep(1)
        print("You win!")
    else:
        time.sleep(1)
        print("You lose!")