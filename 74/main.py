hasla = []

with open('hasla.txt') as file:
    for line in file:
        hasla.append(line.strip())
print(hasla)

ile = 0

for haslo in hasla:
    if haslo.isdecimal():
        ile += 1

print(ile)

dic = {}

for haslo in hasla:
    if haslo in dic:
        dic[haslo] += 1
    else:
        dic[haslo] = 1

for k, v in dic.items():
    if v > 1:
        print(k)

ile = 0


for haslo in hasla:
    num = False
    small = False
    big = False
    for char in haslo:
        if 48 <= ord(char) <= 57:
            num = True
        elif 65 <= ord(char) <= 90:
            big = True
        elif 97 <= ord(char) <= 122:
            small = True
    if num and small and big:
        ile += 1
print(ile)