gol = int(input("Liczba zdobytych goli: "))
punkty_za_gole = gol * 10
bonus = 0

if gol > 10:
    bonus += 10
if gol > 5:
    bonus += 5

wynik_druzyny = punkty_za_gole + bonus

print("\nCałkowity wynik drużyny:", wynik_druzyny)