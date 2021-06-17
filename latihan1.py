kenalan = ["Rafli", "Sultan", "Gagah", "Arya", "Ican"]

print("Isi dari indeks ke-3 adalah " + kenalan[3])

print("Panjang list kenalan: " + format(len(kenalan)))

y = 1
for x in kenalan:
    print("Kenalan ke-" + str(y) + ": " + x)
    y = y + 1