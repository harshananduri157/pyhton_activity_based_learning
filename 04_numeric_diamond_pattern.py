# Case Study 27: Advanced Numeric Pattern Generator
# Heading: Print a Symmetric Number Diamond

n = int(input("Enter the half-height of the diamond (1 to 9): "))

if n < 1 or n > 9:
    print("Please enter a number from 1 to 9.")
else:
    for row in range(1, n + 1):
        print(" " * (n - row), end="")

        for number in range(1, row + 1):
            print(number, end="")

        for number in range(row - 1, 0, -1):
            print(number, end="")

        print()

    for row in range(n - 1, 0, -1):
        print(" " * (n - row), end="")

        for number in range(1, row + 1):
            print(number, end="")

        for number in range(row - 1, 0, -1):
            print(number, end="")

        print()
