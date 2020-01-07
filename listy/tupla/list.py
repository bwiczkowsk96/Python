'1. Utwórz listę o nazwie marketing z elementami:'

'-loyality program'
'-client promotion'
'-market research'

marketing = ['loyality program','client promotion','market resaerch']
marketing.append('public relations')
print(marketing)
print(marketing[2])
marketing.insert(2,'investor relations')

emailMarketing = marketing.copy()
emailMarketing.sort()

internalEmail=['internal communication']

emailMarketing.extend(internalEmail)

emailTuple = tuple(emailMarketing)
print(emailTuple)