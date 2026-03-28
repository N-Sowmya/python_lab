from tkinter import *

root = Tk()
root.title("Tkinter Geometry Manager Example")
root.geometry("350x250")

# ----------------- Using pack() -----------------
label_pack = Label(root, text="This label uses pack()", bg="lightblue")
label_pack.pack(pady=10)

# ----------------- Using place() -----------------
button_place = Button(root, text="Click Me")
button_place.place(x=140, y=150)   # absolute position

root.mainloop()