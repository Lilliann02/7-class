from tkinter import *

root = Tk()
root.title('Мій перший проєкт')
root.geometry('600x400+200+100')
root['bg']='green'
if root['bg']=='green':
    root['bg']='yellow'
button = Button()
button = Button(text='Змінити', width='15',)
button.pack()

root.mainloop()