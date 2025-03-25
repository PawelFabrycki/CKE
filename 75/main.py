with open('tekst.txt') as file:
    teksty = file.readline()

print(teksty)
words = teksty.split()
print(words)

# 75.1
for word in words:
    if word[0] == 'd' and word[-1] == 'd':
        print(word)

# 75.2

def szyfr(napis, a, b):
    result = ""
    for char in napis:
        number = ((ord(char) - 97) * a + b) % 26
        result += chr(number + 97)
    return result

for word in words:
    if len(word) >= 10:
        print(szyfr(word, 5, 2))

# 75.3
with open("probka.txt") as file:
    for line in file:
        napisy = line.split()
        for a in range(26):
            for b in range(26):
                if szyfr(napisy[0], a, b) == napisy[1]:
                    print(napisy, a, b)
                    break
        for a in range(26):
            for b in range(26):
                if szyfr(napisy[1], a, b) == napisy[0]:
                    print(napisy, a, b)
                    break