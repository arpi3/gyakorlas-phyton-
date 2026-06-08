from random import randint

def jotermes(db):
    return db >= 5

gyumolcsfak = ["almafa", "szilvafa", "eperfa", "körtefa", "barackfa", "cseresznyefa"]

gyumolcsfak.append("dijofa")

osszes = 0
jotermesu_fak = 0

for fa in gyumolcsfak:
    termes = randint(1, 10)
    print(f"{fa} - {termes} db termes")

    osszes += termes

    if jotermes(termes):
        jotermesu_fak += 1

atlag = osszes // len(gyumolcsfak)

print(f"osszesen {osszes} db termes volt a kertben")
print(f"atlagosan {atlag} db termes volt a fakon")
print(f"a kertben {jotermesu_fak} db fa volt ami elegendo  termest hozott")




#2.



class Sutemeny:
    def __init__(self, nev: str, tipus: str, ar: int):
        self.nev = nev
        self.tipus = tipus
        self.ar = ar


sutemenyek = []

with open("cuki.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        adatok = sor.strip().split(";")

        nev = adatok[0]
        tipus = adatok[1]
        ar = int(adatok[2])

        sutemenyek.append(Sutemeny(nev, tipus, ar))

print(f"a cuki.txt-ben osszesen {len(sutemenyek)} sutemeny talalhato")

vegyes_osszeg = 0

for suti in sutemenyek:
    if suti.tipus == "vegyes":
        vegyes_osszeg += suti.ar

print(f"a vegyes sutemenyek ara osszesen {vegyes_osszeg} ft")

with open("akciostortak.txt", "w", encoding="utf-8") as fajl:
    for suti in sutemenyek:
        if suti.tipus == "torta" and suti.ar < 10000:
            uj_ar = round(suti.ar * 0.9)

            fajl.write(
                f"{suti.nev};{suti.tipus};{uj_ar}\n"
            )
