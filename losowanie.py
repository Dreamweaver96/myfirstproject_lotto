import random
import time


def losowanie():
    dostepne_liczby = list(range(1, 50))
    wylosowane_liczby = []
    counterek = 0


    while counterek < 6:
        #time.sleep(1.5)
        wylosowana_liczba = random.choice(dostepne_liczby)
        print(wylosowana_liczba)
        print(dostepne_liczby)
        dostepne_liczby.remove(wylosowana_liczba)
        wylosowane_liczby.append(wylosowana_liczba)
        print(f"Wylosowano liczbe " + str(wylosowana_liczba))
        print(dostepne_liczby)
        counterek = counterek + 1

    time.sleep(1.5)
    wylosowane_liczby.sort()
    #str(wylosowane_liczby)
    #print(wylosowane_liczby)
    '''print(f"Wylosowane liczby to: " + str(wylosowane_liczby))'''
    print("Wylosowane liczby to: " + ", ".join(map(str, wylosowane_liczby)))

losowanie()
