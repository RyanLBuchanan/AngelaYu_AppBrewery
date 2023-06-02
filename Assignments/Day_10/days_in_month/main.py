def is_leap(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, further check if it's divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                # If divisible by 400, it's a leap year
                return True
            else:
                # If not divisible by 400, it's not a leap year
                return False
        else:
            # If not divisible by 100, but divisible by 4, it's a leap year
            return True
    else:
        # If not divisible by 4, it's not a leap year
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Check if the year is a leap year and if the month is February (month == 2)
    if is_leap(year) and month == 2:
        # If it's a leap year and February, return 29 days
        return 29
    # Otherwise, return the number of days based on the month from the month_days list
    return month_days[month - 1]

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)