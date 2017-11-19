import datetime
delta = datetime.timedelta(days=10, hours=10, minutes=256, seconds=52)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))
