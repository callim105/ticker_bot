from datetime import date, timedelta


def get_day():
    """
    Returns most recent market day. Does not include Sat/Sunday.
    """
    day = date.today()
    iso_weekday = date.isoweekday(day)
    if iso_weekday == 6:
        day = date.today() - timedelta(days=1)
    elif iso_weekday == 7:
        day = date.today() - timedelta(days=2)
    return day
    
