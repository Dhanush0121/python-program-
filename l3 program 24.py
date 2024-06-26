
import datetime

def findDay(day, month, year):
    # Create a datetime object for the given date
    date = datetime.datetime(year, month, day)

    # Get the weekday as an integer (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    weekday = date.weekday()

    # Define a list of weekday names
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Return the corresponding weekday name based on the weekday index
    return weekdays[weekday]
# Example usage
day = 31
month = 8
year = 2019
result = findDay(day, month, year)
print(result)
