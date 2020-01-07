hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
print(hitsTitles)


hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('Cos tam cos tam')
print(hitsTitles)

hitsTitles.insert(2,'Hotel California')
print(hitsTitles)
hitsTitles.insert(0,'The sound of silence')
print(hitsTitles)

print(hitsTitles.index('Hotel California'))
hitsTitles.remove('Hotel California')
print(hitsTitles)
hitsTitles[0]= 'Enjoy the Silence'
print(hitsTitles)
hitsToRead = hitsTitles.copy()

print(hitsToRead)
hitsToRead.reverse
print(hitsToRead)
hitsToRead.sort()
print(hitsToRead)

hitsToRead.pop(0)
hitsToRead.pop(0)
print(hitsToRead)


additionalSongs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead)
print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))
hitsToRead.clear()
print(hitsToRead)