ciagi = []
with open("ciagi.txt") as file:
    for linia in file:
        liczby = []
        for liczba in linia.split():
            liczby.append(int(liczba))
        if len(liczby) > 1:
            ciagi.append(liczby)


# 61.1
ilosc = 0
maks = 0

for ciag in ciagi:
    roznica = ciag[1] - ciag[0]
    for i in range(1, len(ciag)):
        if roznica != ciag[i] - ciag[i-1]:
            break
    else:
        ilosc += 1
        if roznica > maks:
            maks = roznica

with open("wynik1.txt", "w+") as file:
    file.write(f"Ilość: {ilosc}, Maks różnica: {maks}")

# 61.2

szesciany = []

def szukankoSzescianu(ciag):
    n = 1 
    maksSzescian = 0
    while n**3 <= max(ciag):
        if n**3 in ciag:
            maksSzescian = n**3
        n += 1
    return maksSzescian

for ciag in ciagi:
    szescian = szukankoSzescianu(ciag)
    if szescian != 0:
        szesciany.append(szescian)

with open("wynik2.txt", "w+") as file:
    for s in szesciany:
        file.write(f"{str(s)} \n")

# 61.3

def findBlednyWyrac(ciag):
    for i in range(1, len(ciag)):
        if (ciag[i] - ciag[i-1]) != (ciag[i + 1] - ciag[0]):
            return ciag[i]
    return None

errors = []

for ciag in ciagi:
    error = findBlednyWyrac(ciag)
    if error != None:
        errors.append(error)

with open("wynik3.txt", "w+") as file:
    for s in errors:
        file.write(f"{s} \n")
