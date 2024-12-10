from tkinter import *

def dpl (event):
    root['bg'] = 'yellow'
    root.title("Швидка")
    x = root.winfo_x()
    y = root.winfo_y() + 200
    root.geometry(f'300x300+{x}+{y}')


root=Tk()
root.title('Ліліана')
root.geometry('300x300')
root['bg']='blue'
root.bind('<Double-Button-1>', dpl)

root.mainloop()
