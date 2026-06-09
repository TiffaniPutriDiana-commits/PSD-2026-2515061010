
**Judul Program**

Keranjang Belanja — Implementasi Hash Map Separate Chaining 

Program ini merupakan implementasi struktur data Hash Map dengan metode Separate Chaining menggunakan bahasa pemrograman Python, dengan studi kasus Sistem Keranjang Belanja. Program memungkinkan pengguna menambah, mengurangi, menghapus, dan mencari produk di keranjang, serta melakukan checkout dengan tampilan struk belanja.

Hash Map bekerja dengan memetakan setiap key (ID produk) ke indeks tabel menggunakan fungsi hash, yaitu menjumlahkan nilai ASCII setiap karakter key kemudian dimodulo ukuran tabel (total % SIZE). Ketika dua key menghasilkan indeks yang sama (collision), metode Separate Chaining menanganinya dengan menyimpan node-node tersebut dalam satu linked list di slot yang sama. Kompleksitas rata-rata operasi insert, search, dan delete adalah O(1), namun pada kasus terburuk (semua key bertabrakan) menjadi O(n).

<img width="1453" height="929" alt="Screenshot 2026-06-09 192535" src="https://github.com/user-attachments/assets/4c077ed2-ae81-483c-ad21-faedd5b89f4f" />
<img width="1321" height="852" alt="Screenshot 2026-06-09 192555" src="https://github.com/user-attachments/assets/4cfb87a9-93ce-4328-abd1-1137cb644f8b" />
<img width="1248" height="837" alt="Screenshot 2026-06-09 192624" src="https://github.com/user-attachments/assets/c0e0d038-509d-4b06-a0e0-f3eb2103cce6" />
<img width="1072" height="835" alt="Screenshot 2026-06-09 192719" src="https://github.com/user-attachments/assets/f3cff595-18a7-4739-8538-58d5300fafff" />
<img width="1304" height="843" alt="Screenshot 2026-06-09 192750" src="https://github.com/user-attachments/assets/393a1068-4fea-4a0b-ae50-a6d7c3c2f3fa" />
<img width="1322" height="849" alt="Screenshot 2026-06-09 192811" src="https://github.com/user-attachments/assets/454a80d5-c71d-4e01-9d90-af2aa7500c2e" />
<img width="1293" height="847" alt="Screenshot 2026-06-09 192834" src="https://github.com/user-attachments/assets/4723444a-18d5-4d8c-b4e5-9be3ed1a959e" />
<img width="1312" height="844" alt="Screenshot 2026-06-09 192853" src="https://github.com/user-attachments/assets/6577822f-8f3c-4123-806b-50ae59b1158b" />
<img width="914" height="468" alt="Screenshot 2026-06-09 192905" src="https://github.com/user-attachments/assets/9310d3f7-8518-46cd-8471-d62707c232bc" />

Penjelasa Logika Perbaris : 

Class Node

Baris 2 : class Node: yaitu Mendefinisikan class Node sebagai unit terkecil penyimpanan data dalam linked list di setiap slot hash table

Baris 3 : def __init__(self, key, value): yaitu Konstruktor Node yang menerima key (ID produk) dan value (dictionary berisi data produk)

Baris 4 : self.key = key yaitu Menyimpan key berupa string ID produk (contoh: "P001") sebagai atribut node

Baris 5 : self.value = value yaitu Menyimpan value berupa dictionary {'nama', 'harga', 'jumlah'} sebagai atribut node

Baris 6 : self.next = None yaitu Menginisialisasi pointer next ke None, menandakan belum ada node berikutnya dalam chain

Class HashMapSeparateChaining — Inisialisasi & Fungsi Hash

Baris 10 : class HashMapSeparateChaining: yaitu Mendefinisikan class Hash Map yang menggunakan metode Separate Chaining untuk menangani tabrakan (collision)

Baris 11 : def __init__(self, size=10): yaitu Konstruktor hash map dengan ukuran default 10 slot

Baris 12 : self.SIZE = size yaitu Menyimpan ukuran tabel hash sebagai atribut

Baris 13 : self.table = [None] * self.SIZE yaitu Membuat array dengan SIZE elemen, seluruhnya diinisialisasi None (semua slot kosong)

Baris 16 : def hash_function(self, key): yaitu Mendefinisikan fungsi hash untuk memetakan key string ke indeks slot tabel

Baris 17–19 : total = 0; for karakter in key: total += ord(karakter) yaitu Menjumlahkan nilai ASCII setiap karakter pada key menggunakan fungsi bawaan ord()

Baris 20 : return total % self.SIZE yaitu Mengembalikan sisa bagi total terhadap ukuran tabel sebagai indeks slot yang digunakan


Method insert(self, key, value)
BarisKodePenjelasan

Baris 23 : def insert(self, key, value): yaitu Mendefinisikan method untuk menambah node baru atau memperbarui node yang sudah ada pada hash map

Baris 24 : index = self.hash_function(key) yaitu  Menghitung indeks slot tujuan dengan memanggil fungsi hash

Baris 25 : current = self.table[index] yaitu Mengambil node pertama pada slot tersebut untuk memulai penelusuran chain

Baris 28–32 : while current is not None: if current.key == key: yaitu Menelusuri chain; jika key sudah ada maka value-nya diperbarui (update) lalu fungsi langsung kembali

Baris 35–37 : new_node = Node(key, value) ... self.table[index] = new_node yaitu Jika key belum ada, buat node baru dan sisipkan di depan chain (prepend) agar operasi insert selalu O(1)


Method search(self, key)

Baris 40 : def search(self, key): yaitu Mendefinisikan method untuk mencari node berdasarkan key yang diberikan

Baris 41–42 : index = ... current = ... yaitu Menghitung indeks slot dan mengambil node awal pada slot yang sesuai

Baris 43–46 : while current is not None: if current.key == key: return current yaitu  Menelusuri seluruh node dalam chain; jika key cocok, kembalikan node tersebut

Baris 47 : return None yaitu Mengembalikan None jika key tidak ditemukan di seluruh chain


Method remove_key(self, key)

Baris 50 : def remove_key(self, key): yaitu Mendefinisikan method untuk menghapus node dari hash map berdasarkan key

Baris 54–55 : while current is not None: if current.key == key: yaitu Menelusuri chain; jika key ditemukan, putus sambungan node dari chain

Baris 56-57 :  if prev is None: self.table[index] = current.next yaitu Jika node yang dihapus adalah kepala chain, jadikan node berikutnya sebagai kepala baru

Baris 59 : prev.next = current.nextJika bukan kepala chain, hubungkan node sebelumnya langsung ke node sesudah node yang dihapus

Baris 60 : return True yaitu Mengembalikan True sebagai konfirmasi penghapusan berhasil

Baris 63 : return False yaitu Mengembalikan False jika key tidak ditemukan di tabel

Method display_table(self)

Baris 66 : def display_table(self): yaitu Mendefinisikan method untuk menampilkan seluruh isi struktur hash table, berguna untuk keperluan debug atau verifikasi

Baris 68–78 :  for i in range(self.SIZE): yaitu Iterasi setiap slot tabel dari indeks 0 hingga SIZE-1; jika slot kosong cetak (kosong), jika berisi tampilkan semua node dalam chain dengan format (key, nama) -> hingga None

Class KeranjangBelanja — __init__ & tambah_produk

Baris 82 : class KeranjangBelanja: yaitu Mendefinisikan class keranjang belanja yang menggunakan HashMapSeparateChaining sebagai struktur penyimpanan utama

Baris 83-84 :  def__init__(self) : self.hashmap = HashMapSeparateChaining(size=10) yaitu Membuat instance hash map berukuran 10 slot sebagai atribut keranjang

Baris 87 : def tambah_produk(self, id_produk, nama, harga, jumlah=1): yaitu Mendefinisikan method untuk menambahkan produk ke keranjang; parameter jumlah memiliki nilai default 1

Baris 88 : node = self.hashmap.search(id_produk) yaitu Mencari apakah produk dengan ID tersebut sudah ada di keranjang

Baris 89–93 : if node: node.value['jumlah'] += jumlah yaitu Jika produk sudah ada, cukup tambahkan jumlahnya tanpa membuat entri baru

Baris 96–99 : else: value = {...}; self.hashmap.insert(...) yaitu Jika produk belum ada, buat dictionary value baru lalu masukkan ke hash map dengan insert()

Baris 101-103 : 

Method kurangi_produk(self, id_produk, jumlah=1)

Baris 106 :  def kurangi_produk(self, id_produk, jumlah=1): yaitu Mendefinisikan method untuk mengurangi jumlah produk di keranjang; default pengurangan 1 pcs

Baris 108-111 : if node is None: print([ERROR]); returnValidasi: jika ID produk tidak ditemukan di keranjang, tampilkan pesan error dan hentikan eksekusi

112–114if node.value['jumlah'] <= jumlah: yaitu Jika jumlah yang dikurangi lebih besar atau sama dengan stok di keranjang, hapus produk sepenuhnya menggunakan remove_key()

Baris 116–118 : else: node.value['jumlah'] -= jumlah yaitu Jika stok masih sisa setelah dikurangi, perbarui nilainya saja tanpa menghapus node


Method hapus_produk(self, id_produk)

Baris 121-122 : def hapus_produk(self, id_produk): node = self.hashmap.search(id_produk)
if node is None: yaitu  Mendefinisikan method untuk menghapus produk sepenuhnya dari keranjang tanpa mempedulikan jumlahnya


Baris 123-126 : if node is None: print([ERROR]); return yaitu Validasi: jika ID produk tidak ditemukan, tampilkan pesan error dan hentikan eksekusi

Baris 127–128 : self.hashmap.remove_key(id_produk) yaitu Memanggil remove_key() pada hash map untuk menghapus node produk dari tabel


Method cari_produk(self, id_produk)

Baris 131 : def cari_produk(self, id_produk): yaitu Mendefinisikan method untuk mencari dan menampilkan detail lengkap produk di keranjang

Baris 132 : node = self.hashmap.search(id_produk) yaitu Memanggil search() pada hash map untuk menemukan node dengan key ID produk

Baris 133–140 : if node: print(ID, Nama, Harga, Jumlah, Subtotal) yaitu Jika ditemukan, tampilkan seluruh informasi produk termasuk subtotal hasil perkalian harga dan jumlah

Baris 141-142 : else: print([INFO]) yaitu Jika tidak ditemukan, tampilkan pesan informasi bahwa produk tidak ada di keranjang

Method tampilkan_keranjang(self)

Baris 145 : def tampilkan_keranjang(self): yaitu Mendefinisikan method untuk menampilkan semua produk dalam keranjang berbentuk tabel struk belanja

Baris 146–147 : print("KERANJANG BELANJA ANDA") ... print(header kolom) yaitu Mencetak judul dan header kolom tabel: No, ID, Nama Produk, Harga, Qty, Subtotal

Baris 150 : ada_isi = False yaitu menandai keranjang masih kosong
Baris 151 : total = 0 yaitu untuk menampung akumulasi harga 
Baris 152 : nomor = 1 yaitu  untuk nomor urut tampilan tabel.

Baris 154–157 : for i in range(...): while current is not None: yaitu Iterasi seluruh slot dan chain hash table untuk mengumpulkan semua produk yang tersimpan

Baris 158 :  subtotal = v['harga'] * v['jumlah']  yaitu  Menghitung subtotal setiap baris produk dengan mengalikan harga satuan dan jumlah

Baris 159-162 : total   += subtotal print (...) yaitu  menambahkannya ke total, lalu mencetaknya ke tabel

Baris 167–168 : if not ada_isi: print("(Keranjang kosong)") yaitu Jika tidak ada produk di seluruh tabel, tampilkan keterangan keranjang kosong

Baris 171 : print(f"  {'TOTAL':>42} Rp {total:>9,.0f}") yaitu Mencetak total harga keseluruhan di baris terakhir tabel dengan format rata kanan

Method total_harga(self)

174-175 : def total_harga(self): total=0 yaitu Mendefinisikan method untuk menghitung dan mengembalikan total harga seluruh produk di keranjang

Baris 176–181 : for i in range(...): while current is not None: total += ... yaitu Menelusuri seluruh slot dan chain hash table, mengakumulasi hasil perkalian harga dan jumlah setiap produk

Baris 182 : return total yaitu Mengembalikan nilai total harga sebagai integer

Method checkout(self)

Baris 185 : def checkout(self): yaitu Mendefinisikan method untuk memproses pembayaran dan mengosongkan keranjang setelah transaksi

Baris 186–188 : if self.total_harga() == 0: print([INFO]); return yaitu Validasi: jika keranjang kosong, batalkan proses checkout dan tampilkan pesan informasi

Baris 189 : self.tampilkan_keranjang() yaitu Menampilkan struk belanja lengkap sebelum konfirmasi pembayaran

Baris 190–191 : print(f"Pembayaran ... berhasil.") ... yaitu Mencetak konfirmasi pembayaran berhasil beserta total yang dibayarkan

Baris 193 : self.hashmap.table = [None] * self.hashmap.SIZE yaitu Mereset seluruh slot hash table ke None, mengosongkan keranjang setelah checkout

Fungsi menu()

Baris 197def menu(): yaitu Mendefinisikan fungsi untuk menampilkan daftar pilihan menu utama program setiap iterasi

Baris 198–206 : print("SISTEM KERANJANG BELANJA") ... print("8. Keluar")Yaitu Mencetak 8 opsi menu: tambah, kurangi, hapus, cari, tampilkan keranjang, lihat hash table, checkout, dan keluar

Baris 210 : def main(): yaitu Fungsi utama yang menjalankan seluruh alur program secara interaktif

Baris 211 : keranjang = KeranjangBelanja() yaitu Membuat instance keranjang belanja baru sebagai objek utama program

Baris 214-223 : katalog = {...} yaitu Mendeklarasikan dictionary katalog berisi 8 produk dengan pasangan ID → (nama, harga) sebagai data simulasi

Baris 226–228 : pilih = 0; while pilih != 8: menu() yaitu Perulangan utama program yang terus berjalan sampai pengguna memilih menu 8 (Keluar)

Baris 229–223 : try: pilih = int(input(...)) except ValueError: print(...) yaitu Membaca pilihan menu dari pengguna; jika input bukan angka maka tampilkan error dan ulangi

Baris 236–300 : if pilih == 1: ... elif pilih == 8: yaitu Blok kondisi yang mengarahkan ke method keranjang yang sesuai berdasarkan pilihan menu pengguna


Blok Utama

Baris 303 : if __name__ == "__main__": yaitu Memastikan fungsi main() hanya dijalankan saat file dieksekusi langsung, bukan saat diimpor sebagai modul

Baris 304 : main()Memanggil yaitu  fungsi utama untuk memulai program

link Youtube : 









