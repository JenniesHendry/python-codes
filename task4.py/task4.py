
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
