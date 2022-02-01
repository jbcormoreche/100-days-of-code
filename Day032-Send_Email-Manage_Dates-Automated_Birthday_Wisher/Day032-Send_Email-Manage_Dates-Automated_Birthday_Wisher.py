# Send Email and Manage Dates

# Email SMTP (Simple Mail Transfer Protocol)
# Internet standard communication protocol to send and receive mail messages
import smtplib

my_email = "test@hotmail.fr"
password = "password"

with smtplib.SMTP("smtp.live.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addr="test@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

# datetime module: work with dates and time
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(now, year, month, day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)

# Send motivational quotes on Mondays via email
import datetime as dt
import random
import smtplib

my_email = "test@hotmail.fr"
password = "password"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("./Day032-Send_Email-Manage_Dates-Automated_Birthday_Wisher/quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        mondays_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addr="test@gmail.com",
            msg=f"Subject:Monday Motivation\n\nThis is your quote:\n{mondays_quote}"
        )

# Day 31 Project - Automated Birthday Wisher
from datetime import datetime
import smtplib
import pandas
import random

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("./Day032-Send_Email-Manage_Dates-Automated_Birthday_Wisher/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"./Day032-Send_Email-Manage_Dates-Automated_Birthday_Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    my_email = "test@hotmail.fr"
    password = "password"

    with smtplib.SMTP("smtp.live.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addr=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )
