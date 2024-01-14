import tkinter as tk 
from tkinter import Canvas, Frame
from tkinter import ttk as tkk


def populate(frame):
    '''Put in some fake data'''
    for row in range(100):
        tk.Label(frame, text="%s" % row, width=3, borderwidth="1", 
                relief="solid").grid(row=row, column=0)
        t="this is the second column for row %s" %row
        tk.Label(frame, text=t).grid(row=row, column=1)

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


root = tk.Tk()

canvas = Canvas(master= root,bg="red",height=500)
frame = Frame(canvas, bg="White")
canvas.pack()
canvas.create_window((4,4),window=frame, anchor="nw")


frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)



root.mainloop()