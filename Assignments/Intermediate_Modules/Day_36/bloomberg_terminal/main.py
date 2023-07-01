import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

# Twilio dashboard information
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

NEWS_API_KEY = os.environ['NEWS_API_KEY']
ALPHAVANTAGE_API_KEY = os.environ['ALPHAVANTAGE_API_KEY']

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alphavantage_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": ALPHAVANTAGE_API_KEY,
}

news_parameters = {
    "q": STOCK_NAME,
    "searchIn": "title",
    "from": "2023-06-30",
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}

# Stock API request
stock_response = requests.get(STOCK_ENDPOINT, alphavantage_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
# print(f"Stock data: {stock_data}")
print(stock_data)

# News API request
news_response = requests.get(NEWS_ENDPOINT, news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
# print(f"News data: {news_data}")
print(news_data)

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 
# Send each article as a separate message

# for article in articles:
# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
# message = client.messages \
#     .create(
#     body="",
#     from_="+18554760916",
#     to="+13854329281"
# )
# print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

