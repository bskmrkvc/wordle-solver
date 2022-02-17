reci = []
slovo = "a"
pozicija = 1
listaReci = []

with open('reci.txt') as w:
    reci = w.readlines()

while slovo != '':
    del listaReci[:]
    slovo=input("Unesite neko slovo koje ste probali: ")
    boja=input("Koje je boje? (Y,G,B): ")

    if boja == 'g' or boja == 'G':
        pozicija=int(input("Na kom se mestu nalazi? "))-1
    
    for rec in reci:
        if boja == 'g' or boja == 'G':
            if rec[pozicija]==slovo[0]:
                listaReci.append(rec)
        elif boja == 'b' or boja == 'B':
            if slovo not in rec:
                listaReci.append(rec)
        elif boja =='y' or boja == 'Y':
            if slovo in rec:
                listaReci.append(rec)
    reci=listaReci.copy()
    print(*listaReci)
