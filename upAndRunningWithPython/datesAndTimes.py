from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def main():
    today = date.today()
    print(today, today.day, today.month, today.year)
    print(today.weekday())
    print(datetime.now())
    print("Just the time: ", datetime.time(datetime.now()))

    now = datetime.now()
    # %y/%Y - year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("%Y, %B, %A, %d"))
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("%c, %x, %X"))
    # %I/%H - 12/24 hour, %M - minutes, %S - second, %p locale's AM/PM
    print(now.strftime("%I:%M:%S %p"))

    #timedelta
    print(timedelta(days=365, hours=5, minutes=1))
    print("One year and a week from now will be: " + str(datetime.now() + timedelta(days=365, weeks=1)))
    t = datetime.now() - timedelta(days=5)
    print(t)
    t = datetime.now() + timedelta(6*365/12)
    print(t.strftime("%Y %b %d %H:%M:%S"))
    # How many days until Christmax
    christmaxDay = date(today.year, 12, 25)
    if (today >= christmaxDay):
        christmaxDay = christmaxDay + timedelta(years=1)
    print("There are %d days until Christmax." %(christmaxDay-today).days)

    # a plain text calendar
    c = calendar.TextCalendar(calendar.SUNDAY)
    s = c.formatmonth(2017,1,0,0)
    print(s)
    # a HTML calendar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    hs = hc.formatmonth(2017,1)
    print(hs)
    # loop over the days in a month
    for i in c.itermonthdays(2017,2):
        print(i)
    # print the months and days names
    for name in calendar.month_name:
        print(name)
    for name in calendar.day_name:
        print(name)


if __name__ == "__main__":
    main()

