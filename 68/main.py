def jednolity(napis):
    for i in range(len(napis) - 1):
        if napis[i] != napis[i+1]:
            return False
    return True

napisy = []
with open("dane_napisy.txt") as file:
    for linia in file:
        napisy.append(linia.split())

ilosc = 0
for napis in napisy:
    if napis[0] == napis[1]:
        if jednolity(napis[0]):
            ilosc += 1
print(ilosc)
ilosc = 0

for napis in napisy:
    if sorted(napis[0]) == sorted(napis[1]):
        ilosc += 1
print(ilosc)

# 68.3
napisy = []
with open("dane_napisy.txt") as file:
    for linia in file:
        a, b = linia.strip().split()
        napisy.append(a)
        napisy.append(b)

slownik = {}

for napis in napisy:
    klucz = ''.join(sorted(napis))
    if klucz not in slownik:
        slownik[klucz] = []
    slownik[klucz].append(napis)
k = max(len(value) for value in slownik.values())
print(k)
