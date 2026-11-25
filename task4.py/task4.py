
# 1. List Comprehension
items = [1, 2, 3, 4, 5, 6]

result = [x for x in items if x % 2 == 0]

print("1. Even numbers:", result)


# 2. Dictionary Counting using Counter
from collections import Counter

s = "banana"

counts = Counter(s)

print("2. Character counts:", counts)


# 3. Avoiding Mutable Default Arguments
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print("3. Add item:", add_item("Apple"))
print("   Add another item:", add_item("Banana"))


# 4. Using enumerate()
data = ["Python", "Java", "C++"]

print("4. Enumerate:")
for i, x in enumerate(data):
    print(i, x)


# 5. Using with for File Handling
# Make sure data.txt exists in your project folder.
try:
    with open("data.txt", "r") as f:
        content = f.read()

    print("5. File content:", content)

except FileNotFoundError:
    print("5. File not found: data.txt")


# 6. Object-Oriented Programming
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"


p = Person("Asha")

print("6. Person:", p.greet())


# 7. Proper Exception Handling
value = "123"

try:
    x = int(value)
    print("7. Converted integer:", x)

except ValueError:
    print("7. Invalid integer input")


# 8. Functional Tools - any()
nums = [2, 5, 8, 15, 20]

flag = any(x > 10 for x in nums)

print("8. Any number greater than 10:", flag)


# 9. Using sorted() with key
names = ["john", "Alice", "bob", "David"]

sorted_names = sorted(names, key=str.lower)

print("9. Sorted names:", sorted_names)


# 10. Avoiding Deeply Nested Conditionals
class User:
    def __init__(self, is_active, role):
        self.is_active = is_active
        self.role = role


user = User(True, "admin")

if user and user.is_active and user.role == "admin":
    print("10. Is admin: True")
else:
    print("10. Is admin: False")

# FizzBuzz using a for loop

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

# FizzBuzz using a for loop

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

# FizzBuzz using a for loop

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

# FizzBuzz using a for loop

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

# FizzBuzz using a for loop

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 7

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.")

# Allow 7 attempts
for i in range(1, attempts + 1):

    while True:
        guess = input(f"\nAttempt {i}: Enter your guess: ")

        # Check whether input contains only digits
        if guess.isdigit():
            guess = int(guess)

            if 1 <= guess <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")

        else:
            print("Invalid input! Please enter a numeric value.")

    # Compare the guess with the secret number
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        print(f"You guessed it in {i} attempts.")
        break

    elif guess < secret_number:
        print("Higher! Try a bigger number.")

    else:
        print("Lower! Try a smaller number.")

else:
    # Executes only when all 7 attempts are used without breaking
    print("\nYou lost! Better luck next time.")
    print(f"The correct number was {secret_number}.")

print("\nThanks for playing!")
