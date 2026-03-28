from tkinter import *
from tkinter import messagebox, filedialog

root = Tk()
root.title("GUI Application with Multiple Widgets")
root.geometry("400x350")

# ---------------------------------------
# 1. LISTBOX + SCROLLBAR
# ---------------------------------------
Label(root, text="List of Items:").pack()

frame = Frame(root)
frame.pack()

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, yscrollcommand=scroll.set, height=5)
items = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple"]
for item in items:
    listbox.insert(END, item)
listbox.pack(side=LEFT)

scroll.config(command=listbox.yview)

# ---------------------------------------
# 2. MESSAGE BOX
# ---------------------------------------
def show_message():
    messagebox.showinfo("Message", "Hello! This is a Message Box")

Button(root, text="Show Message Box", command=show_message).pack(pady=5)

# ---------------------------------------
# 3. FILEDIALOG
# ---------------------------------------
def open_file():
    file_path = filedialog.askopenfilename()
    messagebox.showinfo("Selected File", file_path)

Button(root, text="Open File", command=open_file).pack(pady=5)

# ---------------------------------------
# 4. MENU BAR
# ---------------------------------------
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "GUI Application Example"))
menu_bar.add_cascade(label="Help", menu=help_menu)

# ---------------------------------------
# 5. MENUBUTTON
# ---------------------------------------
mb = Menubutton(root, text="Choose Color", relief=RAISED)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

color_var = StringVar()

mb.menu.add_radiobutton(label="Red", variable=color_var, value="Red")
mb.menu.add_radiobutton(label="Blue", variable=color_var, value="Blue")
mb.menu.add_radiobutton(label="Green", variable=color_var, value="Green")

mb.pack(pady=10)

root.mainloop()