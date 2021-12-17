from tkinter import *
from Measurecon import LM
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
g = Entry(root,width=50)
g.pack()
g.insert(1,"Enter quantity of from units.")


def myClick():
    global from_unit
    global to_unit
    global qty
    global result
    instruction = "Click here to convert unit."
    label_1 = Label(root,text="")
    label_1.pack()
    from_unit = f.get()
    to_unit = t.get()
    qty = float(g.get())
    result = float(LM.dispatcher(from_unit,to_unit,qty))
def output():
    global my_output
    top = Toplevel()
    top.geometry("500x500")
    top.title('Results:')
    if qty > result:
        msg = str(qty)+" "+from_unit+" = "+str(result)+" of a "+to_unit
    else:
        msg = str(qty)+" "+from_unit+" contains "+str(result)+"s of "+to_unit
    label_2 = Label(top,text=msg).pack()
    button_2 = Button(top,text="Close window",command=top.destroy).pack()
    

button_1 = Button(root,text="Click here when ready.",command=myClick)
button_1.pack()
button_3 = Button(root,text="View results.",command=output).pack()
button_4 = Button(root,text="Exit",command=root.destroy).pack()

root.mainloop()



