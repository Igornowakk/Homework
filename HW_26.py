
from datetime import datetime, timedelta

def get_date_list(start_date: str, end_date: str) -> list[str]:
    date_lst = [start_date]

    while start_date < end_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        start_date = start_date + timedelta(days=1)
        start_date = datetime.strftime(start_date, "%Y-%m-%d")
        date_lst.append(start_date)

    return date_lst

start_date = "2023-01-01"
end_day = "2023-01-04"
print(get_date_list(start_date, end_day))
