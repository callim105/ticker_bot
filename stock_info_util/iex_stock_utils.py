import os
from pprint import pprint
import requests


def get_news(ticker, IEX_KEY):
    
    try:
        # r = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/batch?types=quote,news,chart&range=10m&last=10&token={IEX_KEY}")    
        r = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/news/last/10?token={IEX_KEY}")
        json_object = r.json()
   
        news_info = json_object
        pprint(json_object)
        for news in news_info[:5]:
            if news['lang'] == "en":
                headline = news['headline']
                source = news['source']
                url = news['url']
                
                news_obj = f"""
            **-------------------------------------------------------------**
            **{headline}**
            News source: **{source}**
            Link: <{url}>
                
                """
                yield news_obj
    except:
        yield "Data not available"

def get_unemployment_rate(IEX_KEY):
    r = requests.get(f"https://cloud.iexapis.com/stable/data-points/market/UNRATE?token={IEX_KEY}")
    return f"The current US unemployment rate is {r.content.decode('utf-8')}%"

def get_price_quote_from_iex(ticker, IEX_KEY):
    r = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={IEX_KEY}")
    json = r.json()
    primary_exchange = json['primaryExchange']
    close_price = json['close']
    latest_time = json['latestTime']
    percent_change = json['changePercent']
    market_cap = json['marketCap']
    ytd_change = json['ytdChange']
    
    payload = f"""
Primary Exchange: {primary_exchange}
Close Price: {close_price}
Latest time priced: {latest_time}
Percent Change: {percent_change}
Market Cap: {market_cap}
YTD Change: {ytd_change}
    """
    
    return payload

