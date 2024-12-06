ciagi = []
with open("ciagi.txt") as file:
    for linia in file:
        liczby = []
        for liczba in linia.split():
            liczby.append(int(liczba))
        if len(liczby) > 1:
            ciagi.append(liczby)
print(ciagi)

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


print(ilosc)
print(maks)

with open("wynik1.txt", "w+") as file:
    file.write(f"Ilość: {ilosc}, Maks różnica: {maks}")
