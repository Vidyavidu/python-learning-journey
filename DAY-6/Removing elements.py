student = {
    "name": "Chinnu",
    "age": 21,
    "course": "CSE"
}

# Remove specific key
student.pop("age")
print(student)

# Remove last inserted item
student.popitem()
print(student)

# Delete using del
del student["name"]
print(student)

# Clear all
student.clear()
print(student)