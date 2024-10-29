x=int(input("Liczba x:"))
y=int(input("Liczba y:"))
z=int(input("Liczba z:"))

if x>y:
    x, y = y, x
if x>z:
    x, z = z, x
if y>z:
    y, z = z, y

print("\nKolejność od najmniejszej do największej:", x, y, z)