import os
from datetime import date, timedelta
from pprint import pprint
import requests

from stock_info_util.date_utils import get_day

ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_KEY")


def get_daily_data(ticker):
    try:
        r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHAVANTAGE_KEY}')
        json_object = r.json()
        pprint(json_object)
        ticker_name = json_object['Meta Data']['2. Symbol']
    
        last_trading_day = str(get_day())
        previous_trading_day = str(get_day() - timedelta(days=1))
        
        daily_closing_price = json_object['Time Series (Daily)'][last_trading_day]['4. close']
        daily_high = json_object['Time Series (Daily)'][last_trading_day]['2. high']
        daily_low = json_object['Time Series (Daily)'][last_trading_day]['3. low']
        daily_volume = int(json_object['Time Series (Daily)'][last_trading_day]['5. volume'])
        
        previous_day_close = float(json_object['Time Series (Daily)'][previous_trading_day]['4. close'])
        percentage_change = ((previous_day_close - float(daily_closing_price))/previous_day_close) * 100
        
        return_data = f"""
        Price Info for {ticker_name.upper()} on {last_trading_day}:
        Closing Price: ${daily_closing_price}
        High Price: ${daily_high}
        Low Price: ${daily_low}
        Daily Volume: {daily_volume:,}
        Percent Change: {round(percentage_change, 2)}%
        """
        return return_data
    except:
        return f"Data for ticker {ticker} not valid."
    
    
def get_current_price(ticker):
    r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={ALPHAVANTAGE_KEY}')
    json_object = r.json()
    
    time_series_data = json_object['Time Series (1min)']
    # Python 3.7 guarantees order of keys, i think?
    most_recent_time = list(time_series_data.keys())[0]
    return round(float(time_series_data[most_recent_time]['4. close']), 2)
    

    
def get_current_price2(ticker):
    r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey={ALPHAVANTAGE_KEY}')
    json_object = r.json()
    
    time_series_data = json_object['Time Series (1min)']
    # Python 3.7 guarantees order of keys, i think?
    most_recent_time = list(time_series_data.keys())[10]
    return round(float(time_series_data[most_recent_time]['4. close']), 2)
    
