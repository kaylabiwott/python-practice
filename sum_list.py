
def sum_list(numbers):
    # Start with zero
    total = 0

    # Go through each number in the list
    for number in numbers:
        # Add the number to the total
        total = total + number

    # Give back the total when done
    return total

# Let's try using the function
my_list = [5, 10, 15]  # This is the list we want to add
result = sum_list(my_list)  # Call the function and store the result

# Show the result on the screen
print("The total sum is:", result)
