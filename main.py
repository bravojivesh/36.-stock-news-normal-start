import requests
from datetime import datetime,timedelta

#jh: news endpoint API key
#Your API key is: 6b439f328fbe4c6387f10f7f2f75b4f7

STOCK_NAME = "TSLA",
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params={"function":"TIME_SERIES_DAILY",
              "symbol":STOCK_NAME,
              "apikey":"XXY80PI9OZJT7VSI"

}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key= "6b439f328fbe4c6387f10f7f2f75b4f7"
news_param={"apiKey":news_api_key,
            "qInTitle":COMPANY_NAME
            }

# API key: XXY80PI9OZJT7VSI. Please record this API key at a safe place for future data access.

#JH: ONLY-----------
# today=datetime.now().date()
# yesterday0=today - timedelta(days=2)
#================================

stock_req = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_json_data = stock_req.json()

# =============
# # print (yesterday0)
# # yesterday=str(yesterday0)
# ====================

print (stock_json_data)
time_series= stock_json_data["Time Series (Daily)"]
print ("Time_series", time_series)
#jh: the above is a dictionary.Accessing the exact value we want is hard. It is much easier
# if it is a list. We can access by index for the last and the previous day.

#jh: we only need values. See the picture in the main folder.
list1=[v for (news_api_key, v) in time_series.items()]
print (list1)
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
value_yesterday=float(list1[0]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
valu_day_before_yest=float(list1[1]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
absolute_diff=abs(value_yesterday-valu_day_before_yest)

print (value_yesterday, valu_day_before_yest,absolute_diff,sep="##")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_in_percent=(absolute_diff/valu_day_before_yest)*100


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if difference_in_percent >0: #made this 0 so that it grabs the data everytime.
    news1 = requests.get(NEWS_ENDPOINT, params=news_param)
    print(news1.json())

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
articles=news1.json()["articles"]
first_three_articles= articles[:3]
print (first_three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
li=[f"Heading: {x['title']} and Desc: {x['description']}" for x in first_three_articles]
print (li)

#TODO 9. - Send each article as a separate message via Twilio. 



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

