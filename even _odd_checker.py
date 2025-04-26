# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Ask the user to input a number
user_input = int(input("Enter a number: "))

# Call the function and print the result
result = check_even_odd(user_input)
print(f"The number {user_input} is {result}.")
