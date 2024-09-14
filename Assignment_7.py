# Prompt user for their name and favorite numbers
name = input("Enter your name: ")
first_number = int(input("Enter your first favorite number: "))
second_number = int(input("Enter your second favorite number: "))
third_number = int(input("Enter your third favorite number: "))

# Store numbers in a list
numbers = [first_number, second_number, third_number]

# Create a list to store tuples of numbers with their even/odd status
status_list = []

# Determine if each number is even or odd
for number in numbers:
    if number % 2 == 0:
        status_list.append((number, "even"))
    else:
        status_list.append((number, "odd"))

# Greet the user
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Print the even/odd status of each number
for number, status in status_list:
    print(f"The number {number} is {status}.")

# Create and print tuples of numbers and their squares
for number in numbers:
    print(f"The number {number} and its square: ({number}, {number ** 2})")

# Calculate the sum of the numbers
total_sum = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

# Check if the sum is a prime number
is_prime = True
if total_sum < 2:
    is_prime = False
else:
    for i in range(2, int(total_sum ** 0.5) + 1):
        if total_sum % i == 0:
            is_prime = False
            break

# Notify user if the sum is a prime number
if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")