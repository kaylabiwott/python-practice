# Function to calculate the factorial of a number
def factorial(number):
    result = 1  # Start with 1 because multiplying by 1 doesn't change the result
    for i in range(1, number + 1):  # Loop from 1 to the number
        result = result * i  # Multiply the result by the current number
    return result  # Return the final result

# Ask the user for a number
number = int(input("Enter a number to calculate its factorial: "))

# Call the factorial function and print the result
print(f"The factorial of {number} is {factorial(number)}")
