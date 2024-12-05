from tkinter import *

def Click (event):
    root['bg'] = 'blue'
    root.title("Лиманка")
    root.geometry('400x300')


root=Tk()
root.title('Ліліана')
root.geometry('200x100')
root['bg']='hot pink'
root.bind('<1>', Click)

root.mainloop()