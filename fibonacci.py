#!/usr/bin/env python3
# Function 1: Validate and return user input
def get_num_terms():
    while True:
        user_input = input("How many Fibonacci terms would you like? ")

        # Check if the input is digits only
        if user_input.isdigit():
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("Error: Please enter a number greater than 0.")
        else:
            print("Error: Please enter a valid positive integer.")


# Function 2: Generate Fibonacci sequence and return list
def generate_fibonacci(n):
    fib_sequence = []

    # Handle first two terms
    a, b = 0, 1

    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b   # update for next term

    return fib_sequence


# Function 3: Print the sequence
def print_sequence(sequence):
    print("Fibonacci sequence:")
    for num in sequence:
        print(num, end=" ")
    print()   # new line at the end


# Main program
def main():
    num_terms = get_num_terms()
    sequence = generate_fibonacci(num_terms)
    print_sequence(sequence)


# Run program
main()
# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
