from random import randint
wynik = randint(1,100)
guessed = False
while not guessed:
    liczba = input("Podaj liczbę")
    try:
        if int(liczba) > wynik:
            print("Za dużo!")
        elif int(liczba) < wynik:
            print("Za mało!")
        else:
            guessed = True
            print("Zgadłeś!")
    except ValueError:
        print("To nie jest liczba!")

