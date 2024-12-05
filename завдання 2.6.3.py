from tkinter import *

def keyPressed (event):
    root['bg'] = 'crimson'
    root.title("Швидка")
    x = root.winfo_x()
    root.geometry(f'300x200+{x}+200')


root=Tk()
root.title('Ліліана')
root.geometry('200x100')
root['bg']='magenta'
root.bind('<KeyPress>', keyPressed)

root.mainloop()
