# Nested for loops.
# Using the outer loop’s variable to control the inner loop’s range().
# Using print("*", end="") to print without moving to a new line.
# Using an empty print() to move to the next line.
print("------ Triangle Pattern Printer -----\n")
height = int(input("Enter desired height of triangle: "))

for i in range(1, height + 1):
    for b in  range(i):
        print("*" ,end=" ")
    print()
