print("Pomyśl liczbę od 0 do 1000, a ja zgadnę ją w max. 10 krokach")
min = 1
max = 1000

for i in range(11):
    guess = int((max - min) / 2 + min)
    print("Zgaduję: " + str(guess))
    answer = input("Zgadłem?")
    if answer == "nie":
        an1 = input("Mniej?")
        if an1 == "tak":
            max = guess - 1
        else:
            an2 = input("Więcej?")
            if an2 == "tak":
                min = guess + 1
            else:
                print("Nie oszukuj!")
    elif answer == "tak":

        print("Wygrałem!")
        break
