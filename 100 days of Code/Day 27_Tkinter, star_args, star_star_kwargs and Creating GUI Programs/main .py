from tkinter import *
window = Tk()

window.geometry('300x100')
window.title("Meter to Km Convert")

my_label1 = Label(text = "Meters", font = ("Arial",18))
my_label1.grid(column=2,row=0)

my_label2 = Label(text = "is equal to", font = ("Arial",18))
my_label2.grid(column=0,row=1)

result = Label(text = "0", font = ("Arial",18))
result.grid(column=1,row=1)

my_label3 = Label(text = "Km.", font = ("Arial",18))
my_label3.grid(column=2,row=1)


def button_clicked():
    result.config(text=(int(input.get())/1000))


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()