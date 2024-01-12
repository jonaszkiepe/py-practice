import requests
from bs4 import BeautifulSoup
import smtplib
import os

url = ("https://www.amazon.com/X-TREXSABER-41inch-Dueling-Changeable-Colors/dp/B09MKG25VD/"
       "ref=sr_1_59?crid=1R9OFZZHZZMWF&keywords=wood%2Bkatana&qid=1698328253&"
       "sprefix=woodkatana%2Caps%2C173&sr=8-59&th=1")

headers = {
 #headers http://myhttpheader.com/
}
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

whole = soup.find("span", class_="a-price-whole").text
decimal = soup.find("span", class_="a-price-fraction").text
price = float(whole + decimal)
if price <= 70:
    product_title = soup.find("span", id="productTitle").text
    msg = "Subject:AMAZON CHEAP PRICE ALERT\n\n" + product_title + "\nis now " + str(price)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user, to_addrs=user, msg=msg)
