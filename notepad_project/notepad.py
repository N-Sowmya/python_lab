import tkinter as tk
from tkinter import filedialog

# creating a window
np=tk.Tk()
np.geometry("500x500")
np.title("Notepad")

#text area
text=tk.Text(np)
text.pack(fill="both",expand=True)

#functions
def new_file():
    text.delete(1.0,tk.END)

def open_file():
    file=filedialog.askopenfilename()
    if file:
        with open(file,'r') as f:
            text.delete(1.0,tk.END)
            text.insert(tk.END,f.read())  

def save_file():
    file=filedialog.asksavesasfilename()
    if file:
        with open(file,'w')as f:
            f.write(text.get(1.0,tk.END))

#menu 
menu=tk.Menu(np)
file_menu= tk.Menu(menu,tearoff=0)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=np.quit)

menu.add_cascade(label="File",menu=file_menu)
np.config(menu=menu)

#run
np.mainloop()