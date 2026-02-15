# Creating a dictionary
student = {
    "id": 101,
    "name": "Sowmya",
    "department": "CSE",
    "marks": 85
}

# a) keys()
print("Keys:", student.keys())

# b) values()
print("Values:", student.values())

# c) items()
print("Items:", student.items())

# d) pop()
removed_value = student.pop("marks")
print("After pop():", student)
print("Popped value:", removed_value)

# e) delete (del)
del student["department"]
print("After delete:", student)
