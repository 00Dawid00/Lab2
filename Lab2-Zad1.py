punkty=int(input("Podaj liczbę zdobytych punktów: "))

if punkty>80:
    print("\nZaliczyłeś/aś egzamin w terminie 0.")
elif 50<=punkty<=80:
    print("\nMożesz poprawić wynik egzaminu.")
else:
    print("\nMusisz poprawić egzamin.")