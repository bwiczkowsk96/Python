data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for dates in data:
    print(dates.upper())


for s in data:
    elements = s.split(':')
    print(elements[1].upper(),elements[1])

for d in data:
    elements = s.split(':')
    if elements[0] =='Error':
        print(elements[1].upper())
    else:
        print(elements[1])