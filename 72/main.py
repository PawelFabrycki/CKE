napisy = []

with open("napisy.txt") as file:
    for line in file:
        a, b = map(str, line.split())
        napisy.append((a, b))

# 72.1

suma = 0
first_pair = None

for a, b in napisy:
    if len(a) >= len(b) * 3 or len(b) >= len(a) * 3:
        suma += 1
        if first_pair is None:
            first_pair = (a, b)

print(suma)
print(first_pair)

# 72.2

for a, b in napisy:

    if b.startswith(a) and len(b) > len(a):
        added = b[len(a):]
        print((a, b), added)

# 72.3

max_len = 0
pary_max = []

for a, b in napisy:
    wspolny = 0
    i = 1
    while i <= min(len(a), len(b)):
        if a[-i] == b[-i]:
            wspolny += 1
            i += 1
        else:
            break

    if wspolny > max_len:
        max_len = wspolny
        pary_max = [(a, b)]
    elif wspolny == max_len and wspolny > 0:
        pary_max.append((a, b))

print(max_len)
for para in pary_max:
    print(para)

# zapisywanie 

with open("wyniki.txt", "w") as out:
    out.write(f"72.1:\nSuma: {suma}, para: {first_pair}\n")
    out.write("\n72.2:\n")
    for a, b in napisy:
        if b.startswith(a) and len(b) > len(a):
            added = b[len(a):]
            out.write(f"{a} {b} {added}\n")

    out.write("\n72.3\n")
    out.write(f"{max_len}\n")
    for a, b in pary_max:
        out.write(f"{a} {b}\n")


