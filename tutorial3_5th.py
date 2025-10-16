# Getting user input and converting it to an int.
# Using a for loop to iterate a specific number of times.
# Managing and updating multiple variables inside a loop to keep track of the state (the previous two numbers).
# Hint: You’ll need two variables to store the two previous numbers in the sequence, let’s call them a and b. Start them at 0 and 1. Inside your loop, you will:
# Print the current value of a.
# Calculate the next number in the sequence (a + b).
# Update a and b for the next iteration. The old b becomes the new a, and the calculated sum becomes the new b. A clever way to do this in Python is with simultaneous assignment: a, b = b, a + b.
print("The Fibonacci Sequence Generator\n")
n = int(input("How many Fibonacci numbers would you like to generate"))
a=0
b=1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c