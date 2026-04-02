student = {
    "name": "Chinnu",
    "age": 21,
    "course": "CSE"
}

# Access using key
print(student["name"])

# Using get()
print(student.get("age"))

# Access non-existing key safely
print(student.get("marks", "Not Found"))