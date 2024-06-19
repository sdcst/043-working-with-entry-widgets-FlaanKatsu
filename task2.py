#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk
from tkinter import *
w = tk.Tk()
w.attributes()
w.geometry()
w.title("Basic Trig Calc")

ins = tk.Label(w,text="INSTRUCTIONS")
insd = tk.Label(w,text="enter the lengh of the 2 short sides of a right triangle.")
s1 = tk.Entry(w)
s2 = tk.Entry(w)
c = tk.Button(w,text="Conpute!")
ansbx = tk.Entry(w)

ansbx.config(state="readonly")


def conpute(s1,s2):
    s32 = (s1**2)+(s2**2)
    s3 = s32**0.5
    s3 = round(s3,2)
    return s3

def do(e):
    s1v = float(s1.get())
    s2v = float(s2.get())
    ans = conpute(s1v,s2v)
    ansbx.config(state='normal')
    ansbx.delete(0,END)
    ansbx.insert(0,ans)
    ansbx.config(state='readonly')


c.bind("<Button-1>",do)

ins.grid(row=1,column=2)
insd.grid(row=2,column=1,columnspan=3)
s1.grid(row=3,column=1)
s2.grid(row=3,column=2)
ansbx.grid(row=3,column=3)
c.grid(row=4,column=2)

w.mainloop()