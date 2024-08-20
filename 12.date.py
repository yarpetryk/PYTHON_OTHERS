from datetime import datetime, timedelta
import time


def get_month():
    date_format = "%B %Y"
    date_format_tariff = "%d/%m/%Y"
    current_month = datetime.now().replace(day=1, hour=1, minute=0, second=0)
    prev_month = (current_month - timedelta(days=1)).replace(day=1, hour=1, minute=0, second=0).strftime(date_format)
    prev_month_first_day = (current_month - timedelta(days=1)).replace(day=1, hour=1, minute=0, second=0).strftime(date_format_tariff)
    timestamp_current_month = current_month.strftime("%s")
    timestamp_prev_month = (current_month - timedelta(days=1)).replace(day=1, hour=1, minute=0, second=0).strftime("%s")
    print({
        "prev_month": prev_month,
        "prev_month_first_day": prev_month_first_day,
        "timestamp_current_month": timestamp_current_month,
        "timestamp_prev_month": timestamp_prev_month
    })
    print(int(time.time()))
    print(datetime.now().strftime("%s"))


get_month()