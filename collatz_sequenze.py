def next_collatz(n):
    if  n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1
def collatz_length(n):
    steps = 0
    while n != 1:
        n = next_collatz(n)
        steps += 1
    return steps
def max_in_collatz(n):
    max_value = n
    while n != 1:
        n = next_collatz(n)
        if n > max_value:
            max_value = n
    return max_value
def print_collatz_sequence(n, max_steps):
    step = 0
    while n != 1 and step < max_steps:
        print(f"Step 0: {n}")
        n = next_collatz(n)
        step += 1
        print(f"Step {step}: {n}")

print("Collatz Sequence Analyzer\n")
print("-" * 25)
print( )
print(f"Steps to reach 1 from 6: {collatz_length(6)}")
print(f"Steps to reach 1 from 7: {collatz_length(7)}")
print(f"Steps to reach 1 from 27: {collatz_length(27)}\n")
print(f"Maximum value in sequence from 27: {max_in_collatz(27)}\n")
print("Collatz sequence starting from 19: ")
print_collatz_sequence(19, 10)
print( )
print("Sequence length comparison: ")
print(f"Starting from 15: {collatz_length(15):} steps")
print(f"Starting from 16: {collatz_length(16):} steps")
print(f"Starting from 17: {collatz_length(17):} steps")