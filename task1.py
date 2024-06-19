"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk
w = tk.Tk()
w.attributes()
w.geometry()
w.resizable(False,False)
w.title("student info entry")

"""
notes: as a bonus, i made a "error: not all fields have been entered!" if the user does not enter all fields,
and made the display entry unmutable. (i like to make sure that UX is always as best i can make it)
"""



name = tk.Label(w,text="Name")
StuN = tk.Label(w,text="Student Number")
Gr = tk.Label(w,text="Grade")
ne = tk.Entry(w)
se = tk.Entry(w)
ge = tk.Entry(w)
do = tk.Button(w,text="Save Info")

data = tk.Entry(width=80)
a = "Data Summary will be showed here."
data.insert(0,a)
data.config(state='readonly')
def ehe(useless):
    dne = ne.get()
    dse = se.get()
    dge = ge.get()
    if dne == "" or dse == "" or dge == "":
        data.config(state='normal')
        data.delete(0,tk.END)
        data.config(state='disabled')
        a = "error: not all fields have been entered!"
    else:
        data.config(state='normal')
        data.delete(0,tk.END)
        data.config(state='disabled')
        a = f"your name is {dne}, your student number is \"{dse}\", and you are in grade {dge}."
    data.config(state='normal')
    data.insert(0,a)
    data.config(state='readonly')
do.bind("<Button-1>",ehe)

data.grid(row=1,column=1,columnspan=3)
name.grid(row=2,column=1)
StuN.grid(row=2,column=2)
Gr.grid(row=2,column=3)
do.grid(row=4,column=2)
ne.grid(row=3,column=1)
se.grid(row=3,column=2)
ge.grid(row=3,column=3)
w.mainloop()