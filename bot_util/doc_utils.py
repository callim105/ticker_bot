
def get_help():
    help_menu = """
    Hello, welcome to Tickerbot. The commands I know are as follows:
Type ! followed by the command name and parameter.


__**Stock Info**__
**!info [ticker]**
    - Shows fundamental data for the stock
**!news [ticker]**
    - Shows latest news articles for the stock

__**Price Data**__
**!daily [ticker]**
    - Shows daily price information for the stock


__**Trading Simulator**__
**!buy [ticker] [quantity]**
    - Buys [quantity] of [shares] for your portfolio.
**!sell [ticker] [quantity]**
    - Sells [quantity] of [shares] for your portfolio.
**!showportfolio**


__**Macro Data**__
**!brokebois**
    - Shows the current US unemployment rate
    """
    
    return help_menu