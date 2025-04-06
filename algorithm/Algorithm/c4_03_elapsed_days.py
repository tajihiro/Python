month_days = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
              [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

def isLeapYear(year):
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        return 1
    return 0

def elapsed_days(year, month, day):
    days = day
    for i in range(month - 1):
        days = days + month_days[isLeapYear(year)][i]
    return days


if __name__ == '__main__':
    print(elapsed_days(2025, 12, 15))