import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 19, 22, 32, 28],
    "Marks": [85, 72, 90, 66, 88]
}

df = pd.DataFrame(data)

print("=== ORIGINAL DATAFRAME ====")
print(df)

# Sorting by a single column
sorted_by_age = df.sort_values(by="Age")
print("\n== SORTED BY AGE (Ascending) ==")
print(sorted_by_age)

# Sorting in descending order
sorted_by_marks_desc = df.sort_values(by="Marks", ascending=False)
print("\n== SORTED BY MARKS (Descending) ==")
print(sorted_by_marks_desc)

# Sorting by multiple columns
sorted_multi = df.sort_values(by=["Age", "Marks"])
print("\n== SORTED BY AGE then MARKS ==")
print(sorted_multi)

# Row slicing using index
print("\n== FIRST 3 ROWS (SLICING) ==")
print(df[0:3])

# Column slicing
print("\n== SELECTING ONLY Name and Marks COLUMNS ==")
print(df[["Name", "Marks"]])

# Conditional slicing
print("\n== SLICING: Students with Marks > 80 ==")
print(df[df["Marks"] > 80])