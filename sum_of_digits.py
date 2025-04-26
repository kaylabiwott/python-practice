# Function to calculate the sum of digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10        # Get the last digit
        total = total + digit # Add it to the total
        n = n // 10           # Remove the last digit
    return total

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Call the function and show the result
print("Sum of digits is:", sum_of_digits(num))
