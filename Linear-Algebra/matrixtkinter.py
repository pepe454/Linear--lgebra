# -*- coding: utf-8 -*-
"""
Matrix Operations GUI
9/29/18
@author: 17Fry
"""

from tkinter import *
import matrix

#windows
window = Tk()
window.geometry('500x500')
window.title("Simple Matrix Operations Interface")

#labels
Label1 = Label(window, text="Create a matrix", font = ("Georgia", 20))
Label1.grid(column=0, row=0)
Label2 = Label(window, text="Number of Rows", font = ("Georgia", 8))
Label2.grid(column=0, row=1)
Label3 = Label(window, text="Number of Columns", font = ("Georgia", 8))
Label3.grid(column=4, row=1)

#entries
numrows = Entry(window,width=10)
numrows.grid(column = 1, row=1)

numcols = Entry(window,width=10)
numcols.grid(column = 5, row=1)

window.mainloop()

