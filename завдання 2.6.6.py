from tkinter import *
from tkinter.messagebox import *

def click (event):
    root.geometry('500x500')
    root['bg'] = 'brown'
    root.title("Проєкт з двома процедурами")
def KeyPress (event):
    showinfo ('інформаційне вікно', 'Я - громадянка України!')
def close (event):
    showinfo ('інформаційне вікно', 'Виконання проєкту закінчено! До побачення!')
root=Tk()
root.bind('<1>', click)
root.bind('<KeyPress>', KeyPress)
root.bind('<Destroy>', close)
root.mainloop()
