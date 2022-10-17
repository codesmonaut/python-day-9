import re

polja = [0, 0, 0, 0, 0, 0, 0, 0, 0]



def get_indeks (koordinate):
    koordinate.strip().upper()

    if len(koordinate) == 2:
        return None

    slovo = koordinate[0] # "B"

    if slovo not in ["A", "B", "C"]:
        return None

    broj_s = koordinate[1] # "3"

    deo1 = { "A": 0, "B": 1, "C": 2 }[slovo]
    deo2 = int(broj_s) - 1

    if deo2 < 0 or deo2 > 2:
        return None

    return deo1 * 3 + deo2



def print_polja (polja):
    def o (vrednost):
        return [" ", "X", "O"][vrednost]

    print()
    print("   1  2  3")
    print(f"A [{o(polja[0])}][{o(polja[1])}][{o(polja[2])}]")
    print(f"B [{o(polja[3])}][{o(polja[4])}][{o(polja[5])}]")
    print(f"C [{o(polja[6])}][{o(polja[7])}][{o(polja[8])}]")
    print()



def get_koordinate_polja ():
    while True:
        unos = input("Unesite koordinate za svoj znak: ").strip().upper()

        provera = re.searh(r'^[ABC][123]$', unos)

        if provera:
            return unos



def is_free (polja, koordinate):
    print("Ovo polje je zauzeto. Izabrite drugo.")
    indeks_polja = get_indeks(koordinate)
    return polja[indeks_polja] == 0



igraci = ["X", "O"]

imena_igraca = []

imena_igraca.append(input("Igrac 1: Unesite svoje ime: "))
imena_igraca.append(input("Igrac 2: Unesite svoje ime: "))

# moguce_koordinate = [
#     ["A1", "A2", "A3"],
#     ["B1", "B2", "B3"],
#     ["C1", "C2", "C3"],

#     ["A1", "B1", "C1"],
#     ["A2", "B2", "C2"],
#     ["A3", "B3", "C3"],

#     ["A1", "B2", "C3"],
#     ["C1", "B2", "A3"]
# ]



def ko_je_pobedio (polja):
    def ko_je_pobedio_u_nizu (polja, niz):
        brojevi = {
            0: 0,
            1: 0,
            2: 0
        }

        for indeks in  niz:
            brojevi[polja[indeks]] += 1

        if brojevi[1] == 3:
            return 1
        
        if brojevi[2] == 3:
            return 2
        
        return 0
    
    moguci_indeksi = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [6, 4, 2]
    ]

    for niz in moguci_indeksi:
        pobednik = ko_je_pobedio_u_nizu(polja, niz)

        if pobednik in [1, 2]:
            return pobednik
        
    return 0



for potez in range(9):
    print_polja(polja)

    indeks_igraca = potez % 2

    ime_igraca = imena_igraca[indeks_igraca]
    znak_igraca = igraci[indeks_igraca]

    print(f"Na redu je: {ime_igraca}.")

    koordinate = get_koordinate_polja()

    while not is_free(polja, koordinate):
        koordinate = get_koordinate_polja()
    
    indeks_polja = get_indeks(koordinate)
    polja[indeks_polja] = indeks_igraca + 1

    pobednik = ko_je_pobedio(polja)

    if pobednik in [1, 2]:
        print(f"Pobedio je igrac {imena_igraca[pobednik - 1]}")
        print_polja(polja)
        break
    
    if potez == 8 and pobednik == 0:
        print_polja(polja)
        print("Nereseno! Niko nije pobedio.")