
---

## 🧪 Latihan 1 – Class & Object
**Hasil:**  
Mengubah `hero1.hp = 500` berhasil.

**Penjelasan:**  
Atribut `hp` bersifat *public*, sehingga dapat diubah langsung dari luar class.

---

## 🧪 Latihan 2 – Interaksi Antar Objek
**Hasil:**  
Hero dapat saling menyerang dan mengurangi HP lawan.

**Penjelasan:**  
Parameter `lawan` harus berupa **objek**, bukan string, agar method dan atribut lawan bisa diakses.

---

## 🧪 Latihan 3 – Inheritance
**Hasil:**  
Jika `super().__init__()` dihapus, muncul error:

**Penjelasan:**  
`super()` digunakan untuk mewarisi atribut dari class induk (`Hero`) ke class anak (`Mage`).

---

## 🧪 Latihan 4 – Encapsulation
**Hasil:**  
Atribut `__hp` tidak bisa diakses langsung, namun bisa melalui getter/setter.

**Catatan:**  
Akses `hero1._Hero__hp` masih bisa karena *name mangling*, tetapi tidak dianjurkan.

**Kesimpulan:**  
Setter penting untuk menjaga integritas data (mencegah HP negatif/cheat).

---

## 🧪 Latihan 5 – Abstraction & Interface
**Hasil:**  
Jika method abstract tidak diimplementasikan, muncul error:

**Penjelasan:**  
Abstract class berfungsi sebagai **kontrak** dan tidak boleh dibuat objek langsung.

---

## 🧪 Latihan 6 – Polymorphism
**Hasil:**  
Berbagai class (`Mage`, `Archer`, `Fighter`, `Healer`) dapat dipanggil dengan method `serang()` yang sama.

**Penjelasan:**  
Polymorphism memungkinkan satu perintah menghasilkan perilaku berbeda tanpa mengubah kode loop.

<img width="396" height="458" alt="image" src="https://github.com/user-attachments/assets/00e56f43-d5b1-4d5a-b648-81088c5993db" />

