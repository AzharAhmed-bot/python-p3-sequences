def print_fibonacci(length):
    n1 = 0
    n2 = 1
    i = 0
    fibonacci_list = []  # Create an empty list to store Fibonacci numbers

    if length <= 0:
        fibonacci_list = []
    elif length == 1:
        fibonacci_list = [0]
    else:
        while i < length:
            fibonacci_list.append(n1)  # Append current Fibonacci number to the list
            nth_term = n1 + n2
            n1 = n2
            n2 = nth_term
            i += 1

    print(fibonacci_list)  # Print the concatenated list of Fibonacci numbers


# Test case
print_fibonacci(2)
