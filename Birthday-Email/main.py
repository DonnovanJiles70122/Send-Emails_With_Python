import smtplib
import datetime as dt
import pandas
import random

# Retrieve current month and day
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# Open CSV file and put the contents into a dictionary
try:
    data = pandas.read_csv("birthdays.csv")
except FileExistsError:
    print("File does not exist")
else:
    birthdays = data.to_dict(orient="records")

# Search the dictionary to see if the current day is 
for date in birthdays:
    if date['month'] == current_month and date['day'] == current_day:
        recipient_name = date['name']

# Create a list on text files and choose a random file name from the list
letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = random.choice(letter_list)

# Open letter text file and read lines from it
file = open(f"letter_templates/{letter}")
lines = file.read()
file.close()

# Replace the string [NAME] with the recipient_name
birthday_email_text = lines.replace("[NAME]", recipient_name)

my_email = "your email"
my_password = "your password"
with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="recipient email", 
        msg=f"Subject:Happy Birthday {recipient_name}\n\n{birthday_email_text}")

