from tkinter import *

window = Tk()
window.title("My First GUI Program")

window.geometry('600x500')

#Label
my_label = Label(text = "I'm a label", font = ("Arial",24))
my_label.pack()

my_label.config(text="New Text")

#Button

def button_clicked():
    my_label.config(text=input.get())
    

button = Button(text="Click me", command=button_clicked)
button.pack()

#input

input = Entry(width=10)
input.pack()

#TextBox
text = Text(height=5,width=30)
text.focus()
text.insert(END,"Example of multi-line text entry")
print(text.get("1.0",END))
text.pack()

#SpinBox

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_ = 0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale

def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#checkbutton

def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkedbutton = Checkbutton(text="Is on?",variable=checked_state,command=checkbutton_used)
checked_state.get()
checkedbutton.pack()

#radiobutton

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="option1",value=1,variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="option2",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple","Banana","Orange","Pear"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit),fruit) 
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()

