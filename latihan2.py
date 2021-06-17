bilangan1 = int(input("Masukkan bilangan ke-1: "))
bilangan2 = int(input("Masukkan bilangan ke-2: "))

def tambah(bil1, bil2):
    hasil = bil1 + bil2
    return hasil

print("Hasil dari", bilangan1, "+", bilangan2, "adalah", tambah(bilangan1, bilangan2))