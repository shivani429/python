from datetime import*
d1=date.today()
print(d1)
d2=d1+timedelta(days=100)
print(d2)
d3=d1+timedelta(weeks=10)
print(d3)
print(d2-d1)
print(d2-d3)