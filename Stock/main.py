import os
import requests
from twilio.rest import Client

TICKER = "AAPL"
COMPANY_NAME = "Apple"
ALPHA_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://www.newsapi.org/v2/everything"
TWILIO_SID = os.getenv("ACCOUNT_SID_TW")
TWILIO_AUTH_TOKEN = os.getenv("AUTH_TOKEN_TW")
TWILIO_NUMBER = os.getenv("NUMBERS_TW")
MY_NUMBER = os.getenv("MY_NUMBER_TW")

#Parametros para Alpha
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": TICKER,
    "apikey": ALPHA_API_KEY,
}


#Response de Alpha
response = requests.get(ALPHA_ENDPOINT,params=parameters)
response.raise_for_status()
time_series = response.json()["Time Series (Daily)"]

close_22 = float(time_series['2025-08-22']['4. close'])
close_21 = float(time_series['2025-08-21']['4. close'])

result = close_22 - close_21
up_or_down = None
if result < 0:
    up_or_down = "⬇️"
else:
    up_or_down = "⬆️"

percentage = round((abs(result) * 100) / close_22, 2)
if percentage > 1:

    # Parámetros para News
    params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=params)
    news_response.raise_for_status()
    apple_news = news_response.json()["articles"]
    three_articles = apple_news[:3]

    formatted_articles = [(f"{TICKER}: {up_or_down}{percentage} \n"
                           f"Headline:{three_articles['title']} \n"
                           f"Description:{three_articles['description']}")
                           for articles in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_ = TWILIO_NUMBER,
            to = TWILIO_NUMBER)
