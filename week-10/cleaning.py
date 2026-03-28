import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", None],
    "Age": [24, None, 22],
    "Marks": [85, 72, None]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. DATAFRAME MODIFICATION

# Add a new column
df["Pass"] = df["Marks"] >= 40
print("\nAfter Adding New Column:")
print(df)

# Update missing values in Age
df["Age"].fillna(df["Age"].mean(), inplace=True)
print("\nAfter Filling Missing Age:")
print(df)

# Modify existing values (Add 5 bonus marks)
df["Marks"] = df["Marks"].fillna(0) + 5
print("\nAfter Updating Marks:")
print(df)

# 2. DATA CLEANING

# Fill missing names with "Unknown"
df["Name"].fillna("Unknown", inplace=True)

# Drop rows with any missing values
clean_df = df.dropna()
print("\nAfter Dropping Rows with Missing Values:")
print(clean_df)