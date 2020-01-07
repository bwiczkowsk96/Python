chanels={'Google' :'1480','Email' :'300','Natural Traffic' :'440','TV Spot' :'700',}
print(chanels['Email'])

newChanels={'Natural Traffic' :'520','News' :'600'}
chanels.update(newChanels)
print(chanels)
print(chanels.keys())
chanels.pop('Email')
print(chanels)