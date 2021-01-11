def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

result = is_leap(int(input("enter year to check if it's a leap year: " )))
print(result)

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month. Try Again."
    monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        return 29
    return monthdays[month - 1]

year = int(input("enter year: "))
month = int(input("enter month: "))
days = days_in_month(year, month)
print(days)
















