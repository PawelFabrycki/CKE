print("Zadanie 60")

liczby = []
licznik = 0
var1 = 0
var2 = 0

with open("liczby.txt", "r") as file:
    for liczba in file:
        liczba = int(liczba)
        if liczba < 1000:
            licznik += 1
            var1 = var2
            var2 = liczba
        liczby.append(liczba)
with open("wyniki.txt", "w+") as file:
    for liczba in liczby:
        file.write(str(liczba) + "\n")
    file.close()

print(licznik)
print(var1, var2)

#podpunkt 60.2

for liczba in liczby:
    dzielniki = []
    for i in range(1, int(liczba ** 0.5)):
        if liczba % i == 0:
            dzielniki.append(i)
            dzielniki.append(liczba // i)
    if liczba % liczba ** 0.5 == 0:
        dzielniki.append(liczba ** 0.5)
    if len(dzielniki) == 18:
        dzielniki.sort()
        print(liczba, dzielniki)



