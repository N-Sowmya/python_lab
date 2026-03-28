from tkinter import *

# Create main window
root = Tk()
root.title("Hello World App")

# Create a label
label = Label(root, text="Hello World", font=("Arial", 20))

# Display the label
label.pack()

# Run the application
root.mainloop()