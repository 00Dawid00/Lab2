litera = input("Wprowadź literę: ")

if litera.isalpha() and len(litera) == 1:
    print("\n" + litera + (" to duża litera." if litera.isupper() else " to mała litera."))
else:
    print("\nWprowadź tylko jedną literę.")