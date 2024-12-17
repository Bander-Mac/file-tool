from tkinter import ttk
from tkinter import *

# Create GUI
root = Tk()
root.title("File Tool")
width = 300
height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - width/2)
center_y = int(screen_height/2 - height/2)
root.geometry(f"{width}x{height}+{center_x}+{center_y}")

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()