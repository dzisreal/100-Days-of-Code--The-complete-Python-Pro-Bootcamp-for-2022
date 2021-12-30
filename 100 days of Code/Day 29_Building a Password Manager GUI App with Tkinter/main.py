from tkinter import *
from tkinter import messagebox
from random import *
import os
os.chdir("C:/Users/Admin/Desktop/100 days of Code/Day 29_Building a Password Manager GUI App with Tkinter")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password will have 6 letters, 6 numbers and 3 symbols
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    for _ in range(6):
        password_list.append(choice(letters))
        password_list.append(choice(numbers))

    for _ in range(3):
        password_list.append(choice(symbols))

    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0,END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    if not website or not email_username or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \n Email: {email_username}"
                                                    f"\n Password: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt","a") as data:
                data.write(f"{website} | {email_username} | {password}\n")
                web_input.delete(0, END)
                password_input.delete(0, END)
                data.close()
                messagebox.showinfo(title="Done", message="Add Successful!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

#Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


#Entries
web_input = Entry(width=50)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_username_input = Entry(width=50)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, 'ndh2912001@gmail.com')

password_input = Entry(width=32)
password_input.grid(row=3, column=1)


#Buttons
generate_pw_button = Button(text="Generate Password", width=14, command=create_password)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()