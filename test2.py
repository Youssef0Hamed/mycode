money = float(input("How much money? "))

if money < 250:
    discount = 1
    print("No discount")
elif money < 500:
    discount = 0.85
    print("15% off")
elif money < 1000:
    discount = 0.80
    print("20% off")
else:
    discount = 0.75
    
    print("25% off")

print("Total after discount:", money * discount)