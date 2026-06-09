
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
BarisKodePenjelasan
2class Node:Mendefinisikan class Node sebagai unit terkecil penyimpanan data dalam linked list di setiap slot hash table

3def __init__(self, key, value):Konstruktor Node yang menerima key (ID produk) dan value (dictionary berisi data produk)

4self.key = keyMenyimpan key berupa string ID produk (contoh: "P001") sebagai atribut node

5self.value = valueMenyimpan value berupa dictionary {'nama', 'harga', 'jumlah'} sebagai atribut node

6self.next = NoneMenginisialisasi pointer next ke None, menandakan belum ada node berikutnya dalam chain

Class HashMapSeparateChaining — Inisialisasi & Fungsi Hash
BarisKodePenjelasan

9class HashMapSeparateChaining:Mendefinisikan class Hash Map yang menggunakan metode Separate Chaining untuk menangani tabrakan (collision)

10def __init__(self, size=10):Konstruktor hash map dengan ukuran default 10 slot

11self.SIZE = sizeMenyimpan ukuran tabel hash sebagai atribut

12self.table = [None] * self.SIZEMembuat array dengan SIZE elemen, seluruhnya diinisialisasi None (semua slot kosong)

14def hash_function(self, key):Mendefinisikan fungsi hash untuk memetakan key string ke indeks slot tabel

15–17total = 0; for karakter in key: total += ord(karakter)Menjumlahkan nilai ASCII setiap karakter pada key menggunakan fungsi bawaan ord()

18return total % self.SIZEMengembalikan sisa bagi total terhadap ukuran tabel sebagai indeks slot yang digunakan


Method insert(self, key, value)
BarisKodePenjelasan

20def insert(self, key, value):Mendefinisikan method untuk menambah node baru atau memperbarui node yang sudah ada pada hash map

21index = self.hash_function(key)Menghitung indeks slot tujuan dengan memanggil fungsi hash

22current = self.table[index]Mengambil node pertama pada slot tersebut untuk memulai penelusuran chain

23–26while current is not None: if current.key == key:Menelusuri chain; jika key sudah ada maka value-nya diperbarui (update) lalu fungsi langsung kembali

27–29new_node = Node(key, value) ... self.table[index] = new_nodeJika key belum ada, buat node baru dan sisipkan di depan chain (prepend) agar operasi insert selalu O(1)


Method search(self, key)
BarisKodePenjelasan

31def search(self, key):Mendefinisikan method untuk mencari node berdasarkan key yang diberikan

32–33index = ... current = ...Menghitung indeks slot dan mengambil node awal pada slot yang sesuai

34–37while current is not None: if current.key == key: return currentMenelusuri seluruh node dalam chain; jika key cocok, kembalikan node tersebut

38return NoneMengembalikan None jika key tidak ditemukan di seluruh chain


Method remove_key(self, key)
BarisKodePenjelasan

40def remove_key(self, key):Mendefinisikan method untuk menghapus node dari hash map berdasarkan key

41–43index = ... current = ... prev = NoneMenghitung indeks, mengambil node awal, dan menyiapkan pointer prev untuk melacak node sebelumnya

44–51while current is not None: if current.key == key:Menelusuri chain; jika key ditemukan, putus sambungan node dari chain

46if prev is None: self.table[index] = current.nextJika node yang dihapus adalah kepala chain, jadikan node berikutnya sebagai kepala baru

48prev.next = current.nextJika bukan kepala chain, hubungkan node sebelumnya langsung ke node sesudah node yang dihapus

50return TrueMengembalikan True sebagai konfirmasi penghapusan berhasil

52return FalseMengembalikan False jika key tidak ditemukan di tabel

Method display_table(self)
BarisKodePenjelasan

54def display_table(self):Mendefinisikan method untuk menampilkan seluruh isi struktur hash table, berguna untuk keperluan debug atau verifikasi

55–64for i in range(self.SIZE):Iterasi setiap slot tabel dari indeks 0 hingga SIZE-1; jika slot kosong cetak (kosong), jika berisi tampilkan semua node dalam chain dengan format (key, nama) -> hingga None

Class KeranjangBelanja — __init__ & tambah_produk
BarisKodePenjelasan

67class KeranjangBelanja:Mendefinisikan class keranjang belanja yang menggunakan HashMapSeparateChaining sebagai struktur penyimpanan utama

69self.hashmap = HashMapSeparateChaining(size=10)Membuat instance hash map berukuran 10 slot sebagai atribut keranjang

71def tambah_produk(self, id_produk, nama, harga, jumlah=1):Mendefinisikan method untuk menambahkan produk ke keranjang; parameter jumlah memiliki nilai default 1

72node = self.hashmap.search(id_produk)Mencari apakah produk dengan ID tersebut sudah ada di keranjang

73–75if node: node.value['jumlah'] += jumlahJika produk sudah ada, cukup tambahkan jumlahnya tanpa membuat entri baru

76–79else: value = {...}; self.hashmap.insert(...)Jika produk belum ada, buat dictionary value baru lalu masukkan ke hash map dengan insert()


Method kurangi_produk(self, id_produk, jumlah=1)
BarisKodePenjelasan

81def kurangi_produk(self, id_produk, jumlah=1):Mendefinisikan method untuk mengurangi jumlah produk di keranjang; default pengurangan 1 pcs

82–84if node is None: print([ERROR]); returnValidasi: jika ID produk tidak ditemukan di keranjang, tampilkan pesan error dan hentikan eksekusi

85–87if node.value['jumlah'] <= jumlah:Jika jumlah yang dikurangi lebih besar atau sama dengan stok di keranjang, hapus produk sepenuhnya menggunakan remove_key()

88–89else: node.value['jumlah'] -= jumlahJika stok masih sisa setelah dikurangi, perbarui nilainya saja tanpa menghapus node


Method hapus_produk(self, id_produk)
BarisKodePenjelasan91def hapus_produk(self, id_produk):Mendefinisikan method untuk menghapus produk sepenuhnya dari keranjang tanpa mempedulikan jumlahnya92–94if node is None: print([ERROR]); returnValidasi: jika ID produk tidak ditemukan, tampilkan pesan error dan hentikan eksekusi95–96self.hashmap.remove_key(id_produk)Memanggil remove_key() pada hash map untuk menghapus node produk dari tabel


Method cari_produk(self, id_produk)
BarisKodePenjelasan

98def cari_produk(self, id_produk):Mendefinisikan method untuk mencari dan menampilkan detail lengkap produk di keranjang

99node = self.hashmap.search(id_produk)Memanggil search() pada hash map untuk menemukan node dengan key ID produk

100–106if node: print(ID, Nama, Harga, Jumlah, Subtotal)Jika ditemukan, tampilkan seluruh informasi produk termasuk subtotal hasil perkalian harga dan jumlah

107else: print([INFO])Jika tidak ditemukan, tampilkan pesan informasi bahwa produk tidak ada di keranjang

Method tampilkan_keranjang(self)
BarisKodePenjelasan

109def tampilkan_keranjang(self):Mendefinisikan method untuk menampilkan semua produk dalam keranjang berbentuk tabel struk belanja

110–111print("KERANJANG BELANJA ANDA") ... print(header kolom)Mencetak judul dan header kolom tabel: No, ID, Nama Produk, Harga, Qty, Subtotal

112–120for i in range(...): while current is not None:Iterasi seluruh slot dan chain hash table untuk mengumpulkan semua produk yang tersimpan

117subtotal = v['harga'] * v['jumlah']Menghitung subtotal setiap baris produk dengan mengalikan harga satuan dan jumlah

121–122if not ada_isi: print("(Keranjang kosong)")Jika tidak ada produk di seluruh tabel, tampilkan keterangan keranjang kosong123print(f"  {'TOTAL':>42} Rp {total:>9,.0f}")Mencetak total harga keseluruhan di baris terakhir tabel dengan format rata kanan

Method total_harga(self)
BarisKodePenjelasan

125def total_harga(self):Mendefinisikan method untuk menghitung dan mengembalikan total harga seluruh produk di keranjang

126–131for i in range(...): while current is not None: total += ...Menelusuri seluruh slot dan chain hash table, mengakumulasi hasil perkalian harga dan jumlah setiap produk

132return totalMengembalikan nilai total harga sebagai integer

Method checkout(self)
BarisKodePenjelasan

134def checkout(self):Mendefinisikan method untuk memproses pembayaran dan mengosongkan keranjang setelah transaksi

135–137if self.total_harga() == 0: print([INFO]); returnValidasi: jika keranjang kosong, batalkan proses checkout dan tampilkan pesan informasi

138self.tampilkan_keranjang()Menampilkan struk belanja lengkap sebelum konfirmasi pembayaran

139–140print(f"Pembayaran ... berhasil.") ...Mencetak konfirmasi pembayaran berhasil beserta total yang dibayarkan

141self.hashmap.table = [None] * self.hashmap.SIZEMereset seluruh slot hash table ke None, mengosongkan keranjang setelah checkout

Fungsi menu() & main()
BarisKodePenjelasan

144def menu():Mendefinisikan fungsi untuk menampilkan daftar pilihan menu utama program setiap iterasi

145–152print("SISTEM KERANJANG BELANJA") ... print("8. Keluar")Mencetak 8 opsi menu: tambah, kurangi, hapus, cari, tampilkan keranjang, lihat hash table, checkout, dan keluar

155def main():Fungsi utama yang menjalankan seluruh alur program secara interaktif

156keranjang = KeranjangBelanja()Membuat instance keranjang belanja baru sebagai objek utama program

157–165katalog = {...}Mendeklarasikan dictionary katalog berisi 8 produk dengan pasangan ID → (nama, harga) sebagai data simulasi

166–167pilih = 0; while pilih != 8:Perulangan utama program yang terus berjalan sampai pengguna memilih menu 8 (Keluar)

168–171try: pilih = int(input(...)) except ValueError:Membaca pilihan menu dari pengguna; jika input bukan angka maka tampilkan error dan ulangi

172–210if pilih == 1: ... elif pilih == 8:Blok kondisi yang mengarahkan ke method keranjang yang sesuai berdasarkan pilihan menu pengguna


Blok Utama
BarisKodePenjelasan
213if __name__ == "__main__":Memastikan fungsi main() hanya dijalankan saat file dieksekusi langsung, bukan saat diimpor sebagai modul

214main()Memanggil fungsi utama untuk memulai program









