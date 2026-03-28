from tkinter import *

root = Tk()
root.title("Checkbutton & Radiobutton Example")

# ---------------------------
# Checkbutton Section
# ---------------------------
Label(root, text="Select Your Hobbies:").pack()

hobby1 = IntVar()
hobby2 = IntVar()

check1 = Checkbutton(root, text="Reading", variable=hobby1)
check2 = Checkbutton(root, text="Music", variable=hobby2)

check1.pack()
check2.pack()

# ---------------------------
# Radiobutton Section
# ---------------------------
Label(root, text="\nSelect Your Gender:").pack()

gender = StringVar()
gender.set("None")

radio1 = Radiobutton(root, text="Male", value="Male", variable=gender)
radio2 = Radiobutton(root, text="Female", value="Female", variable=gender)

radio1.pack()
radio2.pack()

# ---------------------------
# Display Button
# ---------------------------
def show_selection():
    hobbies = []
    if hobby1.get() == 1:
        hobbies.append("Reading")
    if hobby2.get() == 1:
        hobbies.append("Music")

    hobbies_text = ", ".join(hobbies) if hobbies else "None"
    
    output.config(text=f"Hobbies: {hobbies_text}\nGender: {gender.get()}")

Button(root, text="Show Selection", command=show_selection).pack()

# Output label
output = Label(root, text="")
output.pack()

root.mainloop()