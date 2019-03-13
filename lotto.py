from random import randint
lista = []
lista_lotto = []

for i in range(6):
    liczba = input("Podaj liczbę")
    if not liczba.isdigit():
        print ("To nie jest liczba")
        liczba = input("Podaj liczbę")
    if not int(liczba) in range(1, 50):
        print ("Liczba spoza zakresu")
        liczba = input("Podaj liczbę")
    if liczba in lista:
        print ("Ta liczba już była!")
        liczba = input("Podaj liczbę")
        lista.append(liczba)
    else:
        lista.append(liczba)
lista.sort()
a = " ".join(lista)
print(a)

for e in range(6):
    losowanie = randint(1,50)
    lista_lotto.append(str(losowanie))
lista_lotto.sort()
b = " ".join(lista_lotto)
print(b)
trafienia = 0
for n in lista:
    if n in lista_lotto:
        trafienia += 1
if trafienia == 3:
    print("Trafiłeś trójkę!")
elif trafienia == 4:
    print("Trafiłeś czwórkę!")
elif trafienia == 5:
    print("Trafiłeś piątkę!")
elif trafienia == 6:
    print("GRATULACJE!!!")
else:
    print("Tym razem nie wygrałeś :(")


