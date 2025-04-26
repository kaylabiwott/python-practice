# Function to reverse a string
def reverse_string(input_string):
    reversed_string = ""  # Start with an empty string
    # Go through each character from the end to the start manually
    for char in input_string:
        reversed_string = char + reversed_string  # Add each character to the front of the result
    return reversed_string  # Return the reversed string

# Ask the user to input a string
user_input = input("Enter a string to reverse: ")

# Call the function and print the result
print("Reversed string:", reverse_string(user_input))
