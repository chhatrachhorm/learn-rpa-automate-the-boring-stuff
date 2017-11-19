import datetime

print(datetime.datetime.now())
dt = datetime.datetime.now()
print(dt.year, dt.month, dt.hour)

# convert from timestamp
dt = datetime.datetime.fromtimestamp(1000055)
print(dt)

# comparing datetime obj
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)

print(newyears2016 < halloween2015)
