print("-----Running total Calculator-----\n")
total = 0.0
while True:
    number = input("Enter your number or done:")
    if number == "done":
        break
    number = float(number)    
    total = total + number 
    print(f"Your Cuurrent total: {total}")

print(f"Final Sum of all values is: {total}")

