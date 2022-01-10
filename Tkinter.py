import tkinter as tk
import tkinter.scrolledtext as tkst

# Create instance
parent = tk.Tk()
# Add a title
parent.title("Wykop.pl Hity!")

parent.geometry('350x200')
txt = tkst.ScrolledText(parent, width=40, height=10)
txt.grid(column=0, row=0)
txt.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
txt.insert("insert","Hello world!")

# Start GUI
parent.resizable(1,1)
parent.mainloop()