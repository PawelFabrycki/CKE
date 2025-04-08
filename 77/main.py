def szyfrowanko(word, key):
    zaszyfrowane = []
    keyIndex = 0
    for mark in word:
        move = ord(key[keyIndex % len(key)]) - ord('A')
        markZaszyfrowany = chr((ord(mark) - ord('A') + move) % 26 + ord('A'))
        zaszyfrowane.append(markZaszyfrowany)
        keyIndex += 1
    return ''.join(zaszyfrowane)

with open('dokad.txt') as file:
    napis = file.read().strip()

print(napis)

# 77.1

key = "LUBIMYCZYTAC"

# a
print()
# b
print(szyfrowanko(napis, key))


