
MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 10
numr_shares = 100

if num_likes >= MIN_LIKES and numr_shares >= MIN_SHARES:
    print("Dzisiaj obniżka ceny o 10%")
else:
    print("Za mała ilość like")



if num_likes >= MIN_LIKES and numr_shares >= MIN_SHARES:
    print("Dzisiaj obniżka ceny o 10%")

elif num_likes < MIN_LIKES:
    print ('We still need more like')
else:
    print("Za mała ilość like")



print('____________')

isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Dziękujemy dzisiaj otrzymasz kupon na darmowe burgera")
else:
    print("Przykro nam, darmowe burgery są dodawane do zamówienia w tygodniu roboczym")

#ZAGNIEŻDŻONE IF/ELSE
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Dziękujemy dzisiaj otrzymasz kupon na darmowe burgera")

else:

    if isWeekend:
        print('Zamów w tygodniu aby otrzymać znizkę')
    else:
        print("Zamów jeszcze pizze albo burgera")

#ELIF
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Dziękujemy dzisiaj otrzymasz kupon na darmowe burgera")

elif isWeekend:
    print('Please back in non Weekend to get a promotion')

else:
    print('Order Burger or Pizza to get a special prise')




