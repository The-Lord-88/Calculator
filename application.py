from tkinter import Tk, font
from view import View


root = Tk()
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=24)

width = 400
height = 400
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

view = View(root)

root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)
root.mainloop()
