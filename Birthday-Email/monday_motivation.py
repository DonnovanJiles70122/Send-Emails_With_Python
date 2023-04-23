import smtplib
import datetime as dt
import random

now = dt.datetime.now() # create a datetime object
day = now.weekday() # retrieve the current day on the week

# if today's is Monday email quote
if day == 0:
    file = open('quotes.txt', 'r')
    lines = file.readlines()
    quote = random.choice(lines)

    my_email = "my email"
    my_password = "my password"
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="recipient email", 
            msg=f"Subject:Motivation\n\n{quote}")
else: 
    pass
