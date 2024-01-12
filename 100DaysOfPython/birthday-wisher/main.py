import pandas
import datetime as dt
import random
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")

now = dt.datetime.now()
month = now.month
day = now.day

birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")

for birthday in birthdays:
    if birthday["month"] == month and birthday["day"] == day:
        random_letter_index = random.randint(1, 3)
        with open(f"./letter_templates/letter_{random_letter_index}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", birthday["name"])
        msg = f"Subject:Birthday\n\n{letter}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday["email"],
                                msg=msg)

