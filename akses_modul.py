import modul_operasi
modul_operasi.tambah(1,2)
modul_operasi.kurang(1,2)

import modul_operasi as matematika
matematika.tambah(1,3)
matematika.kurang(1,3)

from modul_operasi import tambah
tambah(1,2)

from modul_operasi import tambah, kurang
tambah(1,2)
kurang(1,2)

from modul_operasi import *
tambah(1,2)
kurang(1,2)
