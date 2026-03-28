from tkinter import *

def show_message():
    name = entry.get()       # Get text from entry box
    output_label.config(text="Hello " + name)

# Create main window
root = Tk()
root.title("Simple GUI App")

# Label
label = Label(root, text="Enter your name:")
label.pack()

# Entry
entry = Entry(root)
entry.pack()

# Button
button = Button(root, text="Click Me", command=show_message)
button.pack()

# Output label
output_label = Label(root, text="")
output_label.pack()

# Run window
root.mainloop()