from random import randint
def roll_dice(kod):
    rzuty = kod.split("D")[0]
    if not rzuty:
        rzuty = 1
    rzuty = int(rzuty)


    kostka1 = kod.split("D")[1]
    for kostka in kostka1:
        if "+" in kostka1:
            kostka = kostka1.split("+")[0]
        elif "-" in kostka1:
            kostka = kostka1.split("-")[0]
    kostka = int(kostka)

    for mod in kod:
        if "+" in kod:
            mod = "+" + kod.split("+")[1]
        elif "-" in kod:
            mod = "-" + kod.split("-")[1]
        else:
            mod = 0
    mod = int(mod)

    kostki = [3, 4, 6, 8, 10, 12, 20, 100]

    if kostka  in kostki:
        suma = 0
        for n in range(rzuty):
            oczka = randint(1, kostka)
            suma += oczka
        wynik = suma + mod
        return wynik

    else:
        print("Nie ma takiej kostki!")




print(roll_dice("2D10+10"))
print(roll_dice("D6"))
print(roll_dice("2D3"))
print(roll_dice("D12-1"))
print(roll_dice("D7-1"))


