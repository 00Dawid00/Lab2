punkty=int(input("Podaj liczbę zdobytych punktów: "))

if punkty>80:
    print("Zaliczyłeś/aś egzamin w terminie 0.")
elif 50<=punkty<=80:
    print("Możesz poprawić wynik egzaminu.")
else:
    print("Musisz poprawić egzamin.")