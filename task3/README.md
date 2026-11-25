c = a[:] creates a shallow copy, meaning it creates a new outer list but shares the inner lists with a. Therefore, when a[0][0] changes to 99, the corresponding value in c also changes to 99.

Remember: A shallow copy shares nested objects, while a deep copy creates independent nested objects.

Next, try changing a[0] = [99, 2] and predict what happens to c[0][0].
.copy() makes a *shallow copy*. The outer dictionary is copied,
 but the nested dictionaries inside are NOT duplicated.
 Both 'contacts' and 'copy_contacts' still reference the same inner dicts.
 So changing copy_contacts["c1"]["email"] also changes contacts["c1"]["email"]. -->
Measured Results (typical run on CPython 3.11)
Because no web results were provided, these numbers come from my own knowledge of typical performance on modern Python interpreters:
List membership: ~0.0008 seconds
Set membership: ~0.000003 seconds
Your exact numbers will vary slightly by machine, but the set lookup is usually hundreds of times faster.
 Why the difference? (Time Complexity)
List membership (x in my_list)
Complexity: O(n)
Python checks each element one by one until it finds a match.
For 100,000 items, this means up to 100,000 comparisons.
Set membership (x in my_set)
Complexity: O(1) average
Sets use a hash table, so Python computes the hash of the value and jumps directly to the bucket where it should be stored.
No scanning through elements.
 Summary
Lists: slow membership because they search linearly.
Sets: extremely fast membership because they use hashing.
If you want, I can extend this to compare dictionary lookups or show how performance scales with larger sizes.
List — when you need an ordered, mutable sequence; Tuple — when you need an ordered, immutable grouping; Set — when you need unique items and fast membership tests; Dict — when you need to map keys to values.
 Lists
Lists are best when you need flexible, ordered collections that can grow, shrink, or be modified.
They support indexing, slicing, appending, and removing elements, making them ideal for tasks like building dynamic sequences, processing items in order, or storing data that changes over time.
Lists also preserve insertion order, which matters when the sequence itself carries meaning (e.g., task queues, logs, or ordered results).
 Tuples
Tuples shine when you need fixed, ordered data that should not change after creation.
Their immutability makes them safer for representing structured records (e.g., coordinates, database rows, configuration values) and allows them to be used as dictionary keys or set elements.
Tuples communicate intent: “this grouping is stable,” which helps prevent accidental modification and improves code clarity.
Sets
Sets are ideal when you need unique items and fast membership checks.
They automatically remove duplicates and provide efficient operations like union, intersection, and difference, making them perfect for tasks involving deduplication, comparisons, or filtering.
Because sets are unordered, they are not suitable when the order of elements matters, but they excel in mathematical or logical operations on collections.
Dictionaries
Dictionaries are the right choice when you need to associate keys with values and retrieve data quickly by key.
They are essential for representing structured, labeled information — such as configuration objects, lookup tables,  any scenario where you want meaningful identifiers instead of numeric positions.
Modern Python dicts preserve insertion order, which helps when the order of fields or operations matters.