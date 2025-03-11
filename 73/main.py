with open("tekst.txt") as file:
    tekst = file.readline()
print(tekst)
napisy = tekst.split()
print(napisy)
licznik = 0
for napis in napisy:
    for i in range(len(napis) -1):
        if napis[i] == napis[i+1]:
            licznik += 1
            break
print(licznik)
slownik = {}
for znak in tekst:
    if znak != " " and znak != "\n":
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1
print(sum(slownik.values()))
sortedSlownik = sum(slownik.values())
for tupla in sorted(slownik.items()):
    print(tupla[0], ":", tupla[1], "(", round(100*tupla[1]/sortedSlownik, 2), "%", ")")

samogloski = "AEIOUY"
maks = 0
for napis in napisy:
    n = 0
    for litera in napis:
        if litera not in samogloski:
            n += 1
            if n > maks:
                maks = n
        else:
            n = 0
print(maks)
