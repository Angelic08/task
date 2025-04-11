# Define a range of numbers
start = 1
end = 20

# Separate even and odd numbers
even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)