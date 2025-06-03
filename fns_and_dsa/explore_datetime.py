import datetime as dt


def display_current_datetime():
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_future_date(n):
    return dt.date.today() + dt.timedelta(n)


current_date = display_current_datetime()
print(f"Current date and time: {current_date}")

future_date = calculate_future_date(
    int(input("Enter the number of days to add to the current date: "))
)
print(f"Future date: {future_date}")
