szam = int(input("Kerek egy egyjegyu pozitiv szamot(0-9): "))
while szam < 0 or szam > 9:
    szam = int(input("Kerek egy egyjegyu pozitiv szamot(0-9): "))

if szam > 0 and szam < 9:
    print("az ellenorzott bekeres sikeres!")

if szam % 2 == 0:
    print("a bekert szam (", szam, ") paros")

else:
    print("a bekert szam (", szam, ") paratlan")