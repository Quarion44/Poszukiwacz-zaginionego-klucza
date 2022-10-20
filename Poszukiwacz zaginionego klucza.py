import random
from math import sqrt
from random import randint
import time
import os

clear = lambda: os.system('cls')
clear()

tytul = "POSZUKIWACZ ZAGINIONEGO KLUCZA"
podtytul = "czyli krótka przypowieść o funduszach węglowych"
ver = " v 1.0 "
autor = "by Sławomir Lachowski"
print("="*130)
print("="*130)
print("="*50,tytul,"="*48)
print("="*41,podtytul,"="*40)
print("="*59,ver,"="*62)
print("="*53,autor,"="*54)
print("="*130)
print("="*130)
time.sleep(4)
input("Naciśnij Enter")
clear()

print("="*70)
print()
print("Witaj w Polsce!\n")
print("="*70)
time.sleep(2)

tekst2 = "\nPewna partia polityczna doprowadziła kraj do ruiny. Blackouty zdarzają się coraz częściej. Brak prądu, ogrzewania oraz ciepłej wody to codzienność w życiu przeciętnego Polaka.  \n" \
         "Na szczęście dzięki swojej przenikliwości oraz sprytowi biznesowemu udało Ci się zdobyć wąskotorówkę, którą możesz przerobić na piec. \n" \
         "Jest jednak mały problem.......... " \
         "nie masz pieniędzy na węgiel!!! \n" \
         "Na szczęście przed chwilą zadzwonił do Ciebie prawnik informując o tym, że Twoja ciocia zostawiła Ci spadek w wysokości 1 546 678 złotych i 24 groszy. \n" \
         "To poprawiło Twój humor, bo kupisz za to..... aż 3 tony węgla!!!! Zostanie Ci jeszcze na gumę do żucia, o ile znajdziesz tani skład. \n" \
         "Tylko jest mały problem... \n" \
         "Kasa znajduje się w zamkniętej skrzyni. \n" \
         "Prawnik powiedział, że Twoja ciocia ukryła klucz do tej skrzyni w Twojej piwnicy. \n" \
         "Jest ciemny jesienny wieczór... \n" \
         "Akurat panuje blackout... \n" \
         "Musisz znaleźć klucz za wszelką cenę, więc schodzisz po ciemku do piwnicy. \n" \
         "Tak zaczynają się Twoje poszukiwania klucza, który pozwoli Ci przetrwać zimę!\n\n\n" \
         "W piwnicy znalazł się też przez nikogo nieoczekiwany bohater...\n"

for znak in tekst2:
    print(znak, end='', flush=True)
    time.sleep(0.05)
input("Naciśnij Enter")
clear()

poziom = int(input("Podaj poziom trudności [0 - łatwy, 1 - trudny (bez podpowiedzi): "))
clear()

SZER_GRY = 10
WYS_GRY = 10

x = randint(0, SZER_GRY)
y = randint(0, WYS_GRY)

gracz_x = 0
gracz_y = 0
gracz_get_key = False

kroki = 0

dyst_przed_ruchem = sqrt((x - gracz_x) ** 2 + (y - gracz_y) ** 2)

while not gracz_get_key:
    kroki += 1
    print()
    print("Po piwnicy możesz poruszać się w kierunkach określonych jako litery na klawiaturze: [W, S, A, D]")

    ruch = input("W którą stronę chcesz pójść?: ")

    match ruch.lower():
        case "w":
            gracz_y += 1
            if gracz_y > WYS_GRY:
                print("Gdzie leziesz?! Walnąłeś w ścianę!!!")
                gracz_y = WYS_GRY

        case "s":
            gracz_y -= 1
            if gracz_y < 0:
                print("Gdzie leziesz?! Walnąłeś w ścianę!!!")
                gracz_y = 0

        case "d":
            gracz_x += 1
            if gracz_x > SZER_GRY:
                print("Gdzie leziesz?! Walnąłeś w ścianę!!!")
                gracz_x = SZER_GRY

        case "a":
            gracz_x -= 1
            if gracz_x < 0:
                print("Gdzie leziesz?! Walnąłeś w ścianę!!!")
                gracz_x = 0

        case "q":
            print("Koniec gry!")
            quit()

        case _:
            print("Coś ci się pomieszało, to nie jest kierunek!")
            continue

    if gracz_x == x and gracz_y == y:
        print("*"*70)
        print("UDAŁO SIĘ W", kroki, "KROKACH!!!\n"+"Klucz jest Twój!!!\nMożesz wreszcie kupić węgiel do wąskotorówki!!!")
        if kroki > 17:
            print("\nPonadto zbyt długo łaziłeś po piwnicy, więc zainteresował się Tobą szczur i odgryzł Ci palec u stopy. Ale będziesz żył! Bo to dobry szczurek był.")
        if kroki <= 10 :
            print("\nSzukałeś tak krótko, że szczurek postanowił wyniuchać Ci tani skład węgla. BRAWO!!!")
        print("*"*70)
        print()
        input("Naciśnij Enter aby wyjść z gry")
        quit()

    dyst_po_ruchu = sqrt((x - gracz_x) ** 2 + (y - gracz_y) ** 2)

    if poziom == 0:
        if dyst_po_ruchu < dyst_przed_ruchem:
            print("Szczurek przytakuje: Ciepło!")
        else:
            print("Szczurek kręci głową: Zimno!")
    if poziom == 1:
        l = ["Szczurek wrednie się przygląda", "He he he...", "Skrobu... skrobu... skrobu", "Hihihi", "Zginiesz tutaj...", "Śmieeeeerrrrrćććććć!!!",
             "Wiiiidzęęęę Cięęęęę...", "Mhhhhhh... nowe mięsko", "Cóż to za smakowity kąsek, hm?", "Piiiii piiii piiiii"]
        print(random.choice(l))

    dyst_przed_ruchem = dyst_po_ruchu



