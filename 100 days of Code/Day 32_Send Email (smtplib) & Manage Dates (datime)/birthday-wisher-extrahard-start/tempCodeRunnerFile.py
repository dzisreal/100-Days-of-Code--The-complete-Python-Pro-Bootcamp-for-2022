from datetime import datetime
import pandas
import random
import smtplib
import os
os.chdir("C:/Users/Admin/Desktop/100 days of Code/Day 32_Send Email (smtplib) & Manage Dates (datime)/birthday-wisher-extrahard-start")
MY_EMAIL = "ndh2912001@gmail.com"
MY_PASSWORD = "0987941901"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)