from tkinter import *

def E (event):
    root['bg'] = 'orange'
    x = root.winfo_x() + 300
    root.title("☻♪")
    y = root.winfo_y()
    root.geometry(f'400x300+{x}+{y}')


root=Tk()
root.title('♥☺')
root.geometry('400x300')
root['bg']='hot pink'
root.bind('<Expose>', E)

root.mainloop()
