musclePain = False
fever = True
weakness = True
isMan = True

if musclePain and fever and weakness == True:
    print('suspicion of influenza')

else:
    print('The flu is unlikely')

if musclePain and fever and weakness == True:
    print('suspicion of influenza')

elif not (musclePain and fever) and weakness:
    print('Just take a rest')

else:
    print('Yo maybe cold')

if musclePain and fever and weakness or  isMan and (musclePain or fever or weakness):
    print('It maybe flu')

elif not (musclePain and fever) and weakness:
    print('Just take a rest')

else:
    print('Yo maybe cold')





isCheckCompleted = False

print('Check is completed' if isCheckCompleted == True else 'Check is uncompleted')
