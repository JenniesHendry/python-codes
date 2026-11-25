c = a[:] creates a new outer list, but it does not create copies of the inner lists. Therefore, c and a share the same inner lists, so changing a[0][0] also changes c[0][0].

Key takeaway: This is called a shallow copy.

Try predicting what happens if you change a[0] = [100, 200] instead.
.copy() creates a new outer dictionary, but nested dictionaries remain shared. Therefore, modifying an email in the copied dictionary also modifies the original.

Next practice: Try changing .copy() to copy.deepcopy() and observe whether the original email changes.
List: Python checks elements sequentially until it finds the value.



Set: Uses hashing to locate the value directly, on average.
1.List: Use a list when you need an ordered, changeable collection, e.g., storing students' names in students = ["Asha", "Ravi"].

2. Tuple: Use a tuple when you need an ordered, unchangeable collection, e.g., storing GPS coordinates in location = (10.85, 76.27).

3. Set: Use a set when you need unique values and fast membership testing, e.g., storing unique course IDs in course_ids = {101, 102, 103}.

4. Dict: Use a dictionary when you need key-value pairs for quick lookup, e.g., storing a student's details in student = {"name": "Asha", "age": 21}.