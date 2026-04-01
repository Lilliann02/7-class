from tkinter import*
root = Tk()
root.geometry()

c = Canvas()
c.pack()

c.create_line(230, 200, 210, 180, 190, 180, 230, 150, 210, 120, 170, 130,\
    150, 120, 170, 160, 140, 170, 170, 170, 150, 180, 150, 220, 180, 230, \
    160, 240, 210, 240, 230, 170, 260, 210, 230, 200, 190, 250, fill="orange", width = 10)
root.mainloop()
