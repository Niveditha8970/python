#DateTimr method:-- syntax:- datetime.datetime(year,month,day,time). time formate hours, minutes,seconds

import datetime
sys=datetime.datetime(2022,3,31,12,1,1)
print(sys)

#extract correct time date using now() function

n=datetime.datetime.now()
print(n)

y=datetime.datetime.now().year
print(y)

dy=n.day
print(dy)

dt=n.date
print(dt)

m=n.month
print(m)

t=n.hour
print(t)

mi=n.minute
print(mi)

sc=n.second
print(sc)

#Constrants

my=datetime.MINYEAR
print("minimum year:",my)

mx=datetime.MAXYEAR
print("maxyear:",mx)
