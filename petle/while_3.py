    
import random
my_number = random.randint(0,20)
guess=-1
trials = 0
 
print("Guess my number!")
 
while guess != my_number :
 
    guess = int(input())
    trials+=1
    
    if guess == my_number:
        print("You are right! It was:",my_number, 'Udało Ci się za',trials, 'razem')
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")



