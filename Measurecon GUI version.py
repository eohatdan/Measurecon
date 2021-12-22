from tkinter import *
import argparse
from Measurecon import LM #Import the LM (Liquid Measure) Class
global from_unit
global to_unit
global qty
global lmdict_path
# Allow optional path to lmdict.json to be specified.
parser = argparse.ArgumentParser()
parser.add_argument('--path',nargs='?',const='1',type=str)
args = parser.parse_args()
# Get path to the lmdict.json file.
if args.path == None: # If no --path argument
    lmdict_path = 'lmdict.json' # Use current path
else: # Use the path given by --path <path to lmdict.json>
    lmdict_path = args.path+'lmdict.json'

# Set up GUI window to gather inputs and display output.
root=Tk()
root.geometry("800x800")
f = Entry(root,width=50)
f.pack()
f.insert(0,"Convert from. (e.g., 'Cup')") # Input field for from_unit
t = Entry(root,width=50)
t.pack()
t.insert(1,"Convert to. (e.g., 'Liter')") # Input field for to_uni
g = Entry(root,width=50)
g.pack()
g.insert(1,"Enter quantity of from units.")# Input field for quantity


def myClick(): # Come here when 'Click here when ready' button selected.
    global from_unit
    global to_unit
    global qty
    global result
    label_1 = Label(root,text="")
    label_1.pack()
    from_unit = f.get()
    to_unit = t.get()
    qty = float(g.get())
    result = float(LM.dispatcher(from_unit,to_unit,qty,lmdict_path)) # Do the conversion from_unit to to_unit.
    return
def output(): # Come here when 'View Results' button pressed to display results of converting units.
    global qty
    global result
    top = Toplevel() 
    top.geometry("500x500")
    top.title('Results:')
    if result < 0: # < 0 means unit not found in lm dictionary.
        if result == -1: # From-unit not found.
            msg = "Unable to find '"+from_unit+"' entry in measurements dictionary."
        elif result == -2: # To-unit not found.
            msg = "Unable to find '"+to_unit+"' in measurements dictionary."
        else: msg = "Unknown error converting units." # Unknown error code.
        label_4 = Label(top,text = msg).pack()
        
        button_2 = Button(top,text="Close window",command=top.destroy).pack()
        return
    if qty > result: # Determine type of verb to use, singular or plural
        msg = str(qty)+" "+from_unit+" = "+str(result)+" of a "+to_unit
    else:
        msg = str(qty)+" "+from_unit+" contains "+str(result)+"s of "+to_unit
    label_2 = Label(top,text=msg).pack() # Fill the converted_to field
    # Display number of joules in to_unit
    msg = str(qty)+" of "+to_unit+" contains "+str(LM.convert_to_joules(to_unit,qty))+" joules atm "
    label_3 = Label(top,text=msg).pack() # Fill the energy_units field
    button_2 = Button(top,text="Close window",command=top.destroy).pack()
    return
# Create the client_action buttons.
# The 'command=' field determines the flow of control. 
button_1 = Button(root,text="Click here when ready.",command=myClick).pack()
button_3 = Button(root,text="View results.",command=output).pack()
button_4 = Button(root,text="Exit",command=root.destroy).pack()

root.mainloop()



