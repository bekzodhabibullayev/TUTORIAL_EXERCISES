#TicketPrice
print("-----Movie Ticket Pricer-----\n")
print("Welcome to our Movie Theater, here you can find out prices.\n")
name = input("What is your name: ")
age = int(input("How old are you:\n"))
if age <= 12:
    print(f" Dear {name} , You fall into the 'Children' category.Your ticket price is 8 US dollars!")
elif  13 <= age <= 65:
    print(f" Dear {name}, You fall into the 'Adult' category.Your ticket value is 15 US dollars!")
else:
    print(f"Dear {name}, You fall into the 'Retired' category. Your ticket price is 10 US dollars!")
            