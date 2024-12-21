import requests
import json
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "TLY0L7WIA0UWFOVD"
FILE_PATH = "day 36/stock-news-extrahard-start/stock.json"
News_API_KEY = "0c8d9d9a6b184b82a84e4d5f2c001952"

twilio_sid = " " #Twilio SID 
twilio_auth = " " #Twilio Auth key

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def api_call():
    parameters = {
        "function" : "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "datatype": "json",
        "apikey": API_KEY,
    }

    request_result = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
    request_result.raise_for_status()
    parced_data = request_result.json()
    return parced_data

def read_stock_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    
    return data
def difference():    
    parced_data = read_stock_file(file_path=FILE_PATH)
    last_3_day_data = [day for i, day in enumerate(parced_data["Time Series (Daily)"].items()) if i<2]
    yesterday = last_3_day_data[0][1]
    yesterday_price = float(yesterday["4. close"])
    before_yesterday = last_3_day_data[1][1]
    before_yesterday_price = float(before_yesterday["4. close"])

    percent_change = ((yesterday_price-before_yesterday_price)/before_yesterday_price)*100
    return percent_change
    # if abs(percent_change) > 3:
    #     print("Bring news")
    # else:
    #     print("No significant changes")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news():    
    news_param={
        "q":"Tesla", 
        "pageSize": 3,
        "apiKey": News_API_KEY
    }
    news_api_call = requests.get(url="https://newsapi.org/v2/everything", params=news_param)
    news_api_call.raise_for_status()
    news = news_api_call.json()
    articles = news["articles"]
    return articles

latest_news = get_news()
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
client = Client(twilio_sid, twilio_auth)
message = client.messages.create(
    from_=, #Twilio API 
    to= , #Your Phone number
    body = (
    f"Stock price difference {difference()},\n"
    f"{latest_news[1]['title']}\n"
    f"{latest_news[1]['description']}\n"
    f"{latest_news[1]['url']}"
)
)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

