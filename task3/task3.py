import copy

a = [[1, 2], [3, 4]]
b = a
c = a[:]
d = copy.deepcopy(a)

a[0][0] = 99

print(b[0][0], c[0][0], d[0][0])

# 1. LIST - Ordered and changeable
students = ["Asha", "Ravi", "Meera"]
students.append("Arjun")
print("List:", students)


# 2. TUPLE - Ordered and unchangeable
location = (10.85, 76.27)
print("Tuple:", location)


# 3. SET - Stores unique values
course_ids = {101, 102, 103, 101}
print("Set:", course_ids)

# Fast membership testing
print("Is 102 available?", 102 in course_ids)


# 4. DICTIONARY - Stores key-value pairs
student = {
    "name": "Asha",
    "age": 21,
    "course": "Python"
}

print("Dictionary:", student)

# Access a value using its key
print("Student name:", student["name"])
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing and modifying
print(fruits[1])        # banana
fruits.append("orange") # add item
fruits.remove("banana") # remove item

# Iterating
for f in fruits:
    print(f)
    Creating a tuple
point = (10, 20)

# Accessing
print(point[0])  # 10

# Tuples cannot be modified:
# point[0] = 15  # TypeError

# Useful for fixed records
x, y = point
print(x, y)
Creating a set
colors = {"red", "green", "blue", "red"}  # duplicates removed automatically

print(colors)          # {'red', 'green', 'blue'}
colors.add("yellow")   # add item
colors.discard("green")# remove item safely

# Membership test
print("blue" in colors)  # True

# Set operations
primary = {"red", "blue"}
print(colors.intersection(primary))  # items in both sets
Creating a dictionary
person = {
    "name": "Asha",
    "age": 30,
    "city": "Trivandrum"
}

# Accessing and modifying
print(person["name"])     # Asha
person["age"] = 31        # update value
person["job"] = "Engineer" # add new key-value pair

# Iterating
for key, value in person.items():
    print(key, value)