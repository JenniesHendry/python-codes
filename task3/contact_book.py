import time

contacts = {"9876543210": {"name": "John", "email": "john@gmail.com"},
    "9876543211": {"name": "Smith", "email": "smith@gmail.com"},
    "9876543212": {"name": "Alice", "email": "alice@gmail.com"}}

contacts["9876543213"] = {"name": "David", "email": "david@gmail.com"}
print(contacts.get("9876543210", "Not found"))
print(contacts.get("9876543219", "Not found"))
contacts.pop("9876543212", "Not found")
print(contacts["9876543210"]["email"])
print(contacts.items())
contacts_copy = contacts.copy()
contacts_copy["9876543210"]["email"] = "newjohn@gmail.com"

print("Original email:", contacts["9876543210"]["email"])
print("Copied email:", contacts_copy["9876543210"]["email"])


my_list = list(range(100_000))
my_set = set(my_list)
start = time.perf_counter()
result_list = 99999 in my_list
list_time = time.perf_counter() - start
start = time.perf_counter()
result_set = 99999 in my_set
set_time = time.perf_counter() - start
print("List found:", result_list)
print("List lookup time:", list_time, "seconds")

print("Set found:", result_set)
print("Set lookup time:", set_time, "seconds")
