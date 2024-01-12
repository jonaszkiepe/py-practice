import smtplib
import os




class NotificationManager:
    def __init__(self, flights_data):
        self.email = os.environ.get("MY_EMAIL")
        self.passw = os.environ.get("MY_PASSW")
        self.flights_data = flights_data
        self.send_emails()

    def send_emails(self):
        for flight_data in self.flights_data:
            from_city = flight_data["from"]
            to_city = flight_data["to"]
            price = flight_data["price"]
            link = flight_data["link"]
            date = flight_data["departure"]

            msg = f"Subject: CHEAP FLIGHT ALERT\n\nfrom {from_city} to {to_city} for just {price}$ \ndate: {date}\nlink: {link}"
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.passw)
                connection.sendmail(from_addr=self.email, to_addrs=self.email, msg=msg.encode("utf-8"))
                print("sent")
