ulamki = []
with open("dane_ulamki.txt") as file:
    for line in file.readlines():
        ulamki.append(line.strip().split(" "))

# 65.1 

wartosc = None
najm_ulamek = None

for ulamek in ulamki: 
    ulam = int(ulamek[0]) / int(ulamek[1])
    if wartosc is None or ulam < wartosc or (ulam == wartosc and int(ulamek[1]) < najm_ulamek[1]):
        wartosc = ulam
        najm_ulamek = (int(ulamek[0]), int(ulamek[1]))

print(najm_ulamek)

# 65.2

nieskracalne = 0

for ulamek in ulamki:

    a = int(ulamek[0])
    b = int(ulamek[1])

    while b:
        a, b = b, a % b
        if a == 1:
            nieskracalne += 1
print(nieskracalne)

# 65.3

suma = 0

for ulamek in ulamki:
    a = int(ulamek[0])
    b = int(ulamek[1])
    
    x = a
    y = b

    while y != 0:
        x, y = y, x % y

    nieskracalna = a // x
    suma += nieskracalna

print(suma)

# 65.4

suma_kolejna = 0
b = (2**2) * (3**2) * (5**2) * (7**2) * 13


for ulamek in ulamki:
    a = int(ulamek[0])
    c = int(ulamek[1])
    suma_kolejna += a * (b // c)

print(suma_kolejna)


# zapisywanie

with open('wyniki_ulamki.txt', 'w') as done:
    done.write(f"65.1. {najm_ulamek[0]} {najm_ulamek[1]}\n")
    done.write(f"65.2. {nieskracalne}\n")
    done.write(f"65.3. {suma}\n")
    done.write(f"65.4. {suma_kolejna}\n")
