helloMessage= 'Hello %s!'
print(helloMessage % ('Kate'))
print(helloMessage % ('Chris'))


helloMessage3 = 'Hello {0:s}!'

print(helloMessage3.format('Kate'))


helloMessage='Hello {0:s}!'
print(helloMessage.format('Chris'))

helloMessage="%s has %d %s"
print(helloMessage % ('Kate',1,'animal'))

hellMessage="%s has %d %s"
print(helloMessage %('Chris',100000,'$'))

helloMessage="{0:s} has {1:d} {2:s}"
print(helloMessage.format('Kate',1,'animal'))
print(helloMessage.format('Chris',1000000,'$'))


line= '{0:20s} costs {1:6d} €'
print(line.format('Ice Cream',3))
print(line.format('Trip to Venive', 119))
print(line.format('Pizza Hawai',6))
