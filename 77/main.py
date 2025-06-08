def szyfruj_vigenere(tekst, klucz):
    wynik = []
    klucz_index = 0
    for znak in tekst:
        if 'A' <= znak <= 'Z':
            przesuniecie = ord(klucz[klucz_index % len(klucz)]) - ord('A')
            nowy_znak = chr((ord(znak) - ord('A') + przesuniecie) % 26 + ord('A'))
            wynik.append(nowy_znak)
            klucz_index += 1
        else:
            wynik.append(znak)
    return ''.join(wynik)

def odszyfruj_vigenere(tekst, klucz):
    wynik = []
    klucz_index = 0
    for znak in tekst:
        if 'A' <= znak <= 'Z':
            przesuniecie = ord(klucz[klucz_index % len(klucz)]) - ord('A')
            nowy_znak = chr((ord(znak) - ord('A') - przesuniecie + 26) % 26 + ord('A'))
            wynik.append(nowy_znak)
            klucz_index += 1
        else:
            wynik.append(znak)
    return ''.join(wynik)

def policz_litery(tekst):
    wystapienia = [0]*26
    suma = 0
    for znak in tekst:
        if 'A' <= znak <= 'Z':
            idx = ord(znak) - ord('A')
            wystapienia[idx] += 1
            suma += 1
    return wystapienia, suma

def liczba_powtorzen(ilosc_liter, dlugosc_klucza):
    return (ilosc_liter + dlugosc_klucza - 1) // dlugosc_klucza

def indeks_koincydencji(wystapienia, n):
    licznik = 0
    for l in wystapienia:
        licznik += l*(l-1)
    mianownik = n*(n-1)
    if mianownik == 0:
        return 0
    return licznik/mianownik

def oszacowanie_d(kappa):
    return 0.0285 / (0.0385 - kappa)

# Zadanie 77.1
with open("dokad.txt") as f:
    tekst = f.read().strip()

klucz1 = "LUBIMYCZYTAC"
zaszyfrowany1 = szyfruj_vigenere(tekst, klucz1)
ilosc_liter = sum(1 for c in tekst if 'A' <= c <= 'Z')
powtorzenia = liczba_powtorzen(ilosc_liter, len(klucz1))

# Zadanie 77.2 i 77.3
with open("szyfr.txt") as f:
    szyfr_linia = f.readline().strip()
    klucz2 = f.readline().strip()

odszyfrowany2 = odszyfruj_vigenere(szyfr_linia, klucz2)
wystapienia, suma_liter = policz_litery(szyfr_linia)
kappa = indeks_koincydencji(wystapienia, suma_liter)
szac_dlugosc = oszacowanie_d(kappa)

with open("Vigenere_wyniki.txt", "w") as out:
    out.write("77.1\n")
    out.write(f"a) {powtorzenia}\n")
    out.write(f"b) {zaszyfrowany1}\n\n")

    out.write("77.2\n")
    out.write(odszyfrowany2 + "\n\n")

    out.write("77.3\n")
    out.write("a)\n")
    for i in range(26):
        lit = chr(i + ord('A'))
        out.write(f"{lit}: {wystapienia[i]}\n")
    out.write("\nb)\n")
    out.write(f"Szacunkowa długość klucza: {round(szac_dlugosc, 2)}\n")
    out.write(f"Dokładna długość klucza: {len(klucz2)}\n")

