#1.  (*) - proszę wybacz niepoprawną pisownię lajk i share ;)

#Pracujesz dla firmy odzieżowej, której celem jest wypromowanie nowej kolekcji ubrań.
#  Firma ogłosiła konkurs, który ma na celu zdobywanie "lajków" i "udostępnień" na Facebooku.
#  Jeśli strona firmy otrzyma danego dnia co najmniej 500 "lajków" i co najmniej 100 "udostępnień",
#  to ceny spadną o 10%. Na razie masz napisać fragment programu, który rozstrzygnie czy warunki promocji są spełnione czy nie.
#  Jeśli już wiesz jak to zrobić "GO ON!", a jeśli chcesz, aby Cię trochę pokierować - zajrzyj do kolejnych punktów:

#zadeklaruj zmienną MIN_LIKES  o wartości 500 i MIN_SHARES o wartości 100

#zadeklaruj zmienną num_likes i num_shares o wartościach wskazujących na to ile było kliknięć LIKE i SHARE na Facebooku. 
# Przypisz tym zmiennym wybrane przez CIebie wartości. Zmieniając te wartości będziesz testować poprawność swojego programu,
# np 1300 lajków i 55 sharów

#napisz polecenie IF, które w przypadku spełnienia warunku opisanego na początku, wyświetli komunikat o obniżce ceny, a w przeciwnym razie
#  wyświetli komunikat o braku wystarczającej ilości lajków i sharów

#przetestuj działanie polecenia IF zmieniając wartości zmiennych num_like i num_shares

MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 100000
numr_shares = 100

if num_likes >= MIN_LIKES and numr_shares >= MIN_SHARES:
    print("Dzisiaj obniżka ceny o 10%")
else:
    print("Za mała ilość like")



#2.  Pracujesz dla restauracji, która chce nagrodzić klientów zamawiających w dni robocze (poza weekendem) pizze lub duży napój.
#  Klienci spełniający warunki promocji dostaną kupon na darmowego burgera. Na razie piszesz polecenie decydujące o spełnieniu warunków promocji.
#  Do dyspozycji masz zmienne:

#isPizzaOrdered - o wartości True/False, która informuje, czy klient kupił Pizzę

#isBigDrinkOrdered - o wartości True/False, która informuje, czy klient zamówił duży napój

#isWeekend - o wartości True/False, która informuje, czy jest weekend

#Napisz polecenie IF, które w przypadku, gdy klient kupił pizzę lub duży napój w dzień poza weekendem, wyświetli informację o kuponie na Burgera, 
# a w przeciwnym razie wyświetli komunikat zachęcający do dalszych zakupów.

#Zmieniaj wejściowe warunki logiczne i testuj, czy polecenie zwraca oczekiwany napis.



isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and isWeekend:
    print("Dziękujemy dzisiaj otrzymasz kupon na darmowe burgera")
else:
    print("Przykro nam, darmowe burgery są dodawane do zamówienia w tygodniu roboczym")

