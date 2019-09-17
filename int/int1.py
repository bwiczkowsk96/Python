name = 'Jan'
age = 26
daysInYear = 365
message = '%s is %d years old, so is about %d days old'
print(message % (name,age,age*daysInYear))


name = 'Bartek'
age = 23
daysInYear = 365
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,age*daysInYear))

int2=1234567890
int3=12345

calk=int2//int3
modul=int2%int3

wynik= '{0:d} divided by {1:d} is  {2:d} and the rest is {3:d}'
print(wynik.format(int2,int3,calk,modul))
