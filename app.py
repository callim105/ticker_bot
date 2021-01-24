"""
Ticker Bot - Discord Bot for stocks
"""
import os
import discord 
import logging
from dotenv import load_dotenv
from datetime import date

from stock_info_util.alphavantage_stock_util import get_daily_data
from stock_info_util.mock_trading import buy_stock, sell_stock, get_stocks, test_trades, show_portfolio

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
ALPHAVANTAGE_KEY = os.getenv('ALPHAVANTAGE_KEY')

# logging.basicConfig(filename=)

bot = discord.Client()
mock_trading_db = {}

@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f" {guild.id} (name: {guild.name}")
        guild_count += 1
    print(f"TickerBot is in {guild_count} guilds.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    user = message.author.name
        
    # STOCK PRICE DATA    
    if message.content.startswith('!daily'):
        ticker = message.content.split(' ')[1]
        await message.channel.send(get_daily_data(ticker))  
        
          
    # Mock Trading Simulator
    if message.content.startswith('!buy'):
        
        ticker = message.content.split(' ')[1]
        quantity = int(message.content.split(' ')[2])
      
        buy_stock(user, ticker, quantity, mock_trading_db)
        await message.channel.send(f"Congrats, you bought {quantity} shares of {ticker}. You now have {mock_trading_db[user]['stocks'][ticker]['shares']} shares of {ticker} total!")
        print(mock_trading_db)
    elif message.content.startswith('!sell'):
        ticker = message.content.split(' ')[1]
        quantity = int(message.content.split(' ')[2])
        
        profit = sell_stock(user, ticker, quantity, mock_trading_db)
        await message.channel.send(f"""
            Congrats, you sold {quantity} shares of {ticker}. You now have {mock_trading_db[user]['stocks'][ticker]['shares']} shares of {ticker} total!
            Your profit for this trade is: ${profit}
        """)
    elif message.content.startswith('!showportfolio'):
        for stock_info in show_portfolio(user, mock_trading_db):
            await message.channel.send(stock_info)


bot.run(DISCORD_TOKEN)