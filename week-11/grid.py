from tkinter import *

root = Tk()
root.title("Tkinter Geometry Manager Example")
root.geometry("350x250")

# ----------------- Using grid() -----------------
Label(root, text="Name:", bg="lightyellow").grid(row=0, column=0, padx=10, pady=10)
entry_grid = Entry(root)
entry_grid.grid(row=0, column=1)

# ----------------- Using place() -----------------
button_place = Button(root, text="Click Me")
button_place.place(x=140, y=150)   # absolute position

root.mainloop()