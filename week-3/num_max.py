import numpy as np

# Read data
data = np.array(list(map(int, input("Enter numbers: ").split())))

# Process data
sum = np.sum(data)
avg = np.mean(data)
maximum = np.max(data)

# Display data
print("Data:", data)
print("Sum:", sum)
print("Average:", avg)
print("Maximum:", maximum)