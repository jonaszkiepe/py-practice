import requests
import os
import datetime
import smtplib

today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))
before_yesterday = str(today - datetime.timedelta(days=2))

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API = "https://www.alphavantage.co/query"
NEWS_API = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("STOCK_API_KEY")
}

news_parameters = {
    "apiKey": os.environ.get("NEWS_API_KEY"),
    "q": COMPANY_NAME,
    "from": yesterday,
}

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")


def get_percent_difference():
    stock_response = requests.get(AV_API, params=stock_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()
    time_series = stock_data["Time Series (Daily)"]

    close = "4. close"
    close_before_yesterday = float(time_series[before_yesterday][close])
    close_yesterday = float(time_series[yesterday][close])

    close_difference = close_before_yesterday - close_yesterday
    percent_difference = close_difference/close_before_yesterday * 100
    return percent_difference


def get_news():
    new_response = requests.get(NEWS_API, news_parameters)
    new_response.raise_for_status()
    news = new_response.json()["articles"]
    headlines = []
    descriptions = []
    for article in news[:3]:
        headlines.append(article["title"])
        descriptions.append(article["description"])

    return [headlines, descriptions]


difference = get_percent_difference()
articles = get_news()
article1 = f"Headline: {articles[0][0]}\nBrief: {articles[1][0]}\n\n"
article2 = f"Headline: {articles[0][1]}\nBrief: {articles[1][1]}\n\n"
article3 = f"Headline: {articles[0][2]}\nBrief: {articles[1][2]}\n\n"

if difference >= 5 or difference <= -5:
    if difference >= 5:
        msg = f"Subject:{STOCK} 🔺{round(difference)}%\n\n{article1}{article2}{article3}"
    elif difference <= -5:
        msg = f"Subject:{STOCK} {round(difference)}%\n\n{article1}{article2}{article3}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=msg.encode("utf-8"))
