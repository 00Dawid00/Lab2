litera=input("Wprowadź litere: ")

if litera.isalpha() and len(litera) == 1:
    print(litera, "to duża litera." if litera.isupper() else "to mała litera.")
else:
    print("Wprowadź tylko jedną literę.")