# Fixed spelling: 'balace' → 'balance'
balance = 100

print("Welcome back ❤️")


# deposit
def deposit(amount):
    global balance
    balance += amount
    print(f"Your balance is {balance}")


# spent
def spent(amount):
    global balance

    if amount > balance:
        print("Your balance is not enough")
    else:3
    
    balance -= amount
    print(f"Your balance is {balance}")


while True:
    choice = input("How can I help you?\n1) Deposit\n2) Spend\n3) Exit\n> ")
    if choice == "1":
        amount = int(input("Enter amount: "))
        deposit(amount)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        spent(amount)

    elif choice == "3":

        confirm = input("Do you want to exit? (y/n): ").lower()
        if confirm == "y":
            print("Goodbye 👋")
            break  

    else:
        print("Invalid choice, please try again.")