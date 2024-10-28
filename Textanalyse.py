text = input("Gib einen Text ein: ")

anzahl_woerter = len(text.split())
anzahl_sätze = text.count('.') + text.count('!') + text.count('?')
anzahl_buchstaben = sum(c.isalpha() for c in text)

print(f"Anzahl der Wörter: {anzahl_woerter}")
print(f"Anzahl der Sätze: {anzahl_sätze}")
print(f"Anzahl der Buchstaben: {anzahl_buchstaben}")