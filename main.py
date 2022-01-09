import datetime

year = 197
month = 1
day = 1
d = datetime.datetime(year=year, month=month, day=day)
print(d.timetuple().tm_wday)
