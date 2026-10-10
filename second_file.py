age = 40
print(age>18)

#instrukcja warunkowa
# if-elif-else
#muisi być if ( max jeden), może być 0 do nieskończoności elif, może być 0 lub 1 else

#if warunek:
#.   instukcja ### blok do kykonania?
if age>18:
    print('może kupić browara')
    print('ta linia wykona się tylko jeśli warunek jest spełniony')

age = 15
if age >= 18:
    print('osoba jest pełnoletnia')# musi być jeden
else: # w każdym innym przypadku, jeśli warunek nie jest spełniony
    print('osoba jest niepełnoletnia')# 0 lub 1

#if zawiera warunek, a warunkiem dla else jest przestrzeń rozwiązania

#mamy wyniki egzaminów 100-0

score = 70 
if score >=90:
    print('bardzo dobry')
elif score >=70:
    print('dobry')
elif score >=50:
    print('zaliczenie')
else:
    print('brak zaliczenia')

#and - oba warunki muszą być spełnione
age = 25
has_ticket = False

if age >= 18 and has_ticket: # musi być true and true
    print('może wejść na koncert')
else:
    print('nie może wejść na koncert')  

#or #jeden warunek musi być spełniony

city = 'Karaków'

if city == 'Karaków' or city == 'Warszawa': 
    print('obsługujemy to miasto')
else:
    print('nie obsługujemy tego miasta')

#alternatywa
if city in ['Kraków', 'Warszawa']:
    print('obsługujemy to miasto')
else:
    print('nie obsługujemy tego miasta')

#not - odwrócenie wartości logicznej

is_blocked = False
if not is_blocked: # jeśli nie jest zablokowany
    print('dostęp przyznany')



#1. Napisz taka instrukcje warunkowa, ktora przyznaje dostep, jesli ktos jest > 18; ma subkrypcje i nie jest zablokowany.

age = 13
got_subscription = True
is_blocked = False
if age >= 18 and got_subscription and not is_blocked:
    print('dostęp przyznany')
elif age < 18:
    print('dostęp zabroniony - niepełnoletni')
elif not got_subscription:
    print('dostęp zabroniony - brak subskrypcji')        
else:
    print('dostęp zabroniony')

#Funkcje - chcemy aby framgent wywołać wiele razy
#built in (print) and user defined (musimy napisać sami)

price = 100
quantity = 5
total = price * quantity
print(total)

#definicja funkcji
#def nazwa(argumenty, arg...):
# co się robi z argumentami
def calcualte_total(price, quantity):
    return price*quantity
#wywoływanie
print(calcualte_total(100,10))
print(calcualte_total(20,15))
#return - zwraca wartość poza funkcję

def calcualte_total(price, quantity):
    print(price*quantity)
#return None - jeśli nie ma returna
print(calcualte_total(20,15))   

#połączenie funkcji i instukcji warunkowej

def get_category(score):
    if score >= 80:
        return "high"
    elif score >=50:
        return "medium"
    else:
        return "low"

print(get_category(100))
print(get_category(50))
print(get_category(-10))