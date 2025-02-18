def sumaCyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma

def isPrime(liczba): # liczba jest typu int
    if liczba < 2:
        return False
    elif liczba == 2:
        return True
    elif liczba % 2 == 0:
        return False
    else:
        return True



listaTrojek = []
with open("trojki.txt") as file:
    for linia in file:
        listaTrojek.append(linia.split())
print(listaTrojek)

for liczby in listaTrojek:
    if sumaCyfr(liczby[0]) + sumaCyfr(liczby[1]) == int(liczby[2]):
        print(liczby)