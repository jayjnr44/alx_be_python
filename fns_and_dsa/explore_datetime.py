import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.today()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")
    

display_current_datetime()

No_of_days = int(input("Enter number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.date.today() + timedelta(days=No_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

calculate_future_date()


# date = datetime.datetime.now()
# print(date)