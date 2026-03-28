import pandas as pd

# Define the file path (replace 'data.csv' with your file path if needed)
file_path = r'C:\Users\Navya\OneDrive\Desktop\25335A0517\python_lab\week-10\data.csv'

# 1. Import data from CSV to DataFrame using read_csv()
try:
    df = pd.read_csv(file_path) #
    print(f"Successfully imported data from {file_path}\n")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    print("Please make sure the CSV file is in the correct path and try again.")
    exit()

# 2. Inspect data in the DataFrame

print("--- Inspecting the DataFrame ---")

# Use head() to view the first few rows (default is 5, can specify an integer, e.g., df.head(10))
print("\n* First 5 rows of the DataFrame (df.head()):")
print(df.head())

# Use tail() to view the last few rows (default is 5, can specify an integer, e.g., df.tail(10))
print("\n* Last 5 rows of the DataFrame (df.tail()):")
print(df.tail())

# Use info() to get a concise summary of the DataFrame (data types, non-null counts, memory usage, etc.)
print("\n* DataFrame information (df.info()):")
df.info()

# Use describe() to generate descriptive statistics for numerical columns (mean, std, min, max, quartiles)
print("\n* Descriptive statistics of the DataFrame (df.describe()):")
print(df.describe())
