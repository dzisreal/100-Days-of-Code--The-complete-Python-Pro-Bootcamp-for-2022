from tkinter import *
from tkinter import messagebox
from random import *
import os
os.chdir("C:/Users/Admin/Desktop/100 days of Code/Day 29_Building a Password Manager GUI App with Tkinter")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Password will have 6 letters, 6 numbers and 3 symbols
# def create_password():
password_list = []
for _ in range(6):
    password_list.append(choice(letters))
    password_list.append(choice(numbers))

for _ in range(3):
    password_list.append(choice(symbols))

password = ""
for i in password_list:
    password+=i
print(password)