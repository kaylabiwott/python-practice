def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get a number from the user
n = int(input("Enter a number: "))

# Print the result
print("Factorial is:", factorial(n))
