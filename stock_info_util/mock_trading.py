"""
Methods to handle mock trading
"""
from stock_info_util.alphavantage_stock_util import get_current_price
from pprint import pprint

"""
{callim: {
        'profit': 0,
        'stocks': {
            'AMD': {
                'shares': 500,
                'total_cost': 10000
            }
        }
    }
}
"""

def init_user(user_id, db):
    db[user_id] = {'profit': 0, 'stocks': {}}
    

def buy_stock(user_id, ticker, quantity, db):
    current_stock_price = get_current_price(ticker)
    total_cost = current_stock_price * int(quantity)
    
    if user_id not in db:
        init_user(user_id, db)
        db[user_id]['stocks'][ticker] = {}
        db[user_id]['stocks'][ticker]['shares'] = quantity
        db[user_id]['stocks'][ticker]['avg_price_per_share'] = current_stock_price
        db[user_id]['stocks'][ticker]['total_cost'] = total_cost
    elif user_id in db and db[user_id]['stocks'].get(ticker) is None:
        db[user_id]['stocks'][ticker] = {}
        db[user_id]['stocks'][ticker]['shares'] = quantity
        db[user_id]['stocks'][ticker]['avg_price_per_share'] = current_stock_price
        db[user_id]['stocks'][ticker]['total_cost'] = total_cost
        
    else:
        new_total_shares = db[user_id]['stocks'][ticker]['shares'] + quantity
        new_average_price = (db[user_id]['stocks'][ticker]['total_cost'] + (current_stock_price * quantity))/new_total_shares
        db[user_id]['stocks'][ticker]['shares'] = new_total_shares
        db[user_id]['stocks'][ticker]['total_cost'] += total_cost
        db[user_id]['stocks'][ticker]['avg_price_per_share'] = new_average_price
    pprint(db)
        

def sell_stock(user_id, ticker, quantity, db):
    current_stock_price = get_current_price(ticker)
    total_cost = current_stock_price * int(quantity)
    
    if user_id not in db:
        init_user(user_id, db)
        return "https://media.giphy.com/media/d68K4eApIUez3rkmcV/giphy.gif"
    elif user_id in db and db[user_id]['stocks'].get(ticker) is None:
        return "https://media.giphy.com/media/d68K4eApIUez3rkmcV/giphy.gif"
    else:
        current_stock_val = db[user_id]['stocks'][ticker]['total_cost']
        avg_price = db[user_id]['stocks'][ticker]['avg_price_per_share']
        profit = total_cost - (avg_price * quantity)
        
        if int(quantity) > db[user_id]['stocks'][ticker]['shares']:
            return f"Can't sell more than you own. Total shares owned of {ticker}: {db[user_id]['stocks'][ticker]['shares']}"
        
        db[user_id]['stocks'][ticker]['shares'] -= quantity
        db[user_id]['stocks'][ticker]['total_cost'] -= total_cost
        db[user_id]['profit'] += profit
        return profit

def get_stocks(user_id, db):
    if user_id not in db:
        init_user(user_id, db)
    else:
        return db[user_id]['stocks']


def show_portfolio(user_id, db):
    if user_id not in db:
        init_user(user_id, db)
        return "You have no stock"
    
    stocks = get_stocks(user_id, db)
    for ticker in stocks:
        yield f"{ticker} | Shares: {stocks[ticker]['shares']}"

def test_trades():
    
    db = {}
    buy_stock('callim', 'AMD', 1000, db)
    for stock in show_portfolio('callim', db):
        print(stock)