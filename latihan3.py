bilangan1 = int(input("Masukkan bilangan ke-1: "))
bilangan2 = int(input("Masukkan bilangan ke-2: "))
operasi = input("Masukkan operasi: ")

def tambah(bil1, bil2):
    hasil = bil1 + bil2
    return hasil

def kurang(bil1, bil2):
    hasil = bil1 - bil2
    return hasil

def bagi(bil1, bil2):
    hasil = bil1 // bil2
    return hasil

def kali(bil1, bil2):
    hasil = bil1 * bil2
    return hasil

if(operasi == "+"):
    print("Hasil dari", bilangan1, "+", bilangan2, "adalah", tambah(bilangan1, bilangan2))
elif(operasi == "-"):
    print("Hasil dari", bilangan1, "-", bilangan2, "adalah", kurang(bilangan1, bilangan2))
elif(operasi == "/"):
    print("Hasil dari", bilangan1, "/", bilangan2, "adalah", bagi(bilangan1, bilangan2))
elif(operasi == "*"):
    print("Hasil dari", bilangan1, "*", bilangan2, "adalah", kali(bilangan1, bilangan2))
else:
    print("Operasi salah")