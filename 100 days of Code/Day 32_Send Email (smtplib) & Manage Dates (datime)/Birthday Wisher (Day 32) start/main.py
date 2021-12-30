#------------------------Send Email--------------------------#
import smtplib
def send_email(text):
    my_email = "ndh2912001@gmail.com"
    password = "0987941901"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg="Subject:Test\n"+text)
        connection.close()


#-------------------------DateTime----------------------------#
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

with open("C:/Users/Admin/Desktop/100 days of Code/Day 32_Send Email (smtplib) & Manage Dates (datime)/Birthday Wisher (Day 32) start/quotes.txt") as data:
    lst_quotes = data.readlines()
    quotes = [random.choice(lst_quotes) for i in range(day_of_week)]
    text = random.choice(quotes)
    send_email(text)


