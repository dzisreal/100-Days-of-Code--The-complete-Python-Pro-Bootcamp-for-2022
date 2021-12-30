from tkinter import *
from tkinter import messagebox
from random import *
import os
import json
os.chdir("C:/Users/Admin/Desktop/100 days of Code/Day 30_Errors, Exceptions and Json Data_Improving the Password/Password+Manager+(End+of+Day+29)")
with open("data.json","r") as data:
    data_load = json.load(data)
    lst = list(i for i in data_load)
    print(lst)
