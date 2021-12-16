from tkinter import *

global from_unit
global to_unit
root=Tk()
root.geometry("800x800")
f = Entry(root,width=50)
f.pack()
f.insert(0,"Convert from. (e.g., 'Cup')")
t = Entry(root,width=50)
t.pack()
t.insert(1,"Convert to. (e.g., 'Liter')")


def myClick():
    global from_unit
    global to_unit
    instruction = "Click here to convert unit."
    label_1 = Label(root,text="")
    label_1.pack()
    from_unit = f.get()
    to_unit = t.get()
    

def output():
    global my_output
    top = Toplevel()
    top.geometry("500x500")
    top.title('Results:')
    
    label_2 = Label(top,text=from_unit +" "+to_unit).pack()
    button_2 = Button(top,text="Close window",command=top.destroy).pack()
    

button_1 = Button(root,text="Click here when ready.",command=myClick)
button_1.pack()
button_3 = Button(root,text="View results.",command=output).pack()
button_4 = Button(root,text="Exit",command=root.destroy).pack()

root.mainloop()
print("From: "+from_unit+" to: "+to_unit)
from Measurecon import LM
LM.dispatcher()
