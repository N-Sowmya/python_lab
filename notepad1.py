import tkinter as tk

#create a window
np=tk.Tk()
np.title("NOtepad")
np.geometry("500x500")

#label
label1=tk.Label(np,text="Notepad", font=("Arial",12))
label1.pack()
#text 
text=tk.Text(np,font=("Arial",12))
text.pack(fill="both",expand=True)

#run
np.mainloop()