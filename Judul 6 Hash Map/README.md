
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
BarisKodePenjelasan5class Node:Mendefinisikan class Node sebagai unit penyimpanan data dalam linked list di setiap slot hash table6def __init__(self, key, value):Konstruktor Node yang menerima key (ID produk) dan value (dictionary data produk)7self.key = keyMenyimpan key (ID produk, misal "P001") sebagai atribut node8self.value = valueMenyimpan value berupa dictionary {'nama', 'harga', 'jumlah'} sebagai atribut node9self.next = NoneMenginisialisasi pointer next ke None, menandakan belum ada node berikutnya dalam chain

Class HashMapSeparateChaining — Inisialisasi & Hash Function
BarisKodePenjelasan12class HashMapSeparateChaining:Mendefinisikan class Hash Map yang menggunakan metode Separate Chaining untuk menangani collision13def __init__(self, size=10):Konstruktor hash map dengan ukuran default 10 slot14self.SIZE = sizeMenyimpan ukuran tabel hash15self.table = [None] * self.SIZEMembuat array dengan SIZE slot, seluruhnya diinisialisasi None (kosong)17def hash_function(self, key):Mendefinisikan fungsi hash untuk memetakan key string ke indeks tabel18–19for karakter in key: total += ord(karakter)Menjumlahkan nilai ASCII setiap karakter pada key menggunakan fungsi ord()20return total % self.SIZEMengembalikan sisa bagi total terhadap ukuran tabel sebagai indeks slot

Method insert(self, key, value)
BarisKodePenjelasan22def insert(self, key, value):Mendefinisikan method untuk menambah atau memperbarui data pada hash map23index = self.hash_function(key)Menghitung indeks slot dengan memanggil fungsi hash24current = self.table[index]Mengambil node pertama di slot tersebut untuk traversal25–28while current is not None: if current.key == key:Menelusuri chain; jika key sudah ada, value-nya diperbarui (update) lalu fungsi kembali29–31new_node = Node(key, value) ... self.table[index] = new_nodeJika key belum ada, buat node baru dan sisipkan di depan chain (prepend)

Method search(self, key)
BarisKodePenjelasan33def search(self, key):Mendefinisikan method untuk mencari node berdasarkan key34–35index = ... current = ...Menghitung indeks dan mengambil node awal pada slot yang sesuai36–39while current is not None:Menelusuri seluruh node dalam chain sampai key ditemukan atau chain habis38return currentMengembalikan node yang ditemukan40return NoneMengembalikan None jika key tidak ditemukan

Method remove_key(self, key)
BarisKodePenjelasan42def remove_key(self, key):Mendefinisikan method untuk menghapus node berdasarkan key43–45index = ... current = ... prev = NoneMenghitung indeks, mengambil node awal, dan menyiapkan pointer prev untuk traversal46–52while current is not None: if current.key == key:Menelusuri chain; jika key ditemukan, putus sambungan node dari chain48if prev is None: self.table[index] = current.nextJika node yang dihapus adalah node pertama, jadikan node berikutnya sebagai kepala chain50prev.next = current.nextJika bukan node pertama, hubungkan node sebelumnya langsung ke node sesudah node yang dihapus53return TrueMengembalikan True sebagai tanda penghapusan berhasil
55return FalseMengembalikan False jika key tidak ditemukan

Method display_table(self)
BarisKodePenjelasan57def display_table(self):Mendefinisikan method untuk menampilkan seluruh isi struktur hash table (keperluan debug)58–67for i in range(self.SIZE):Iterasi setiap slot tabel; jika kosong cetak (kosong), jika berisi tampilkan semua node dalam chain dengan format (key, nama) ->


Class KeranjangBelanja — tambah_produk
BarisKodePenjelasan70class KeranjangBelanja:Mendefinisikan class keranjang belanja yang menggunakan HashMapSeparateChaining sebagai penyimpanan data71self.hashmap = HashMapSeparateChaining(size=10)Membuat instance hash map berukuran 10 sebagai atribut keranjang73def tambah_produk(self, id_produk, nama, harga, jumlah=1):Mendefinisikan method untuk menambahkan produk ke keranjang, default jumlah 1 pcs74node = self.hashmap.search(id_produk)Mencari apakah produk dengan ID tersebut sudah ada di keranjang75–77if node: node.value['jumlah'] += jumlahJika produk sudah ada, cukup tambahkan jumlahnya tanpa membuat entri baru78–81else: ... self.hashmap.insert(...)Jika produk belum ada, buat dictionary value baru dan masukkan ke hash map


Method kurangi_produk & hapus_produk
BarisKodePenjelasan83def kurangi_produk(self, id_produk, jumlah=1):Mendefinisikan method untuk mengurangi jumlah produk di keranjang84–86if node is None: print([ERROR])Validasi: jika ID produk tidak ditemukan di keranjang, tampilkan pesan error87–89if node.value['jumlah'] <= jumlah:Jika jumlah yang dikurangi ≥ stok di keranjang, hapus produk seluruhnya menggunakan remove_key()90–91else: node.value['jumlah'] -= jumlahJika masih ada sisa, kurangi jumlahnya saja93def hapus_produk(self, id_produk):Mendefinisikan method untuk menghapus produk sepenuhnya dari keranjang terlepas dari jumlahnya


Method cari_produk
BarisKodePenjelasan100def cari_produk(self, id_produk):Mendefinisikan method untuk mencari dan menampilkan detail produk di keranjang101node = self.hashmap.search(id_produk)Memanggil method search() pada hash map untuk mencari node dengan key ID produk102–108if node: print(...)Jika ditemukan, tampilkan ID, nama, harga, jumlah, dan subtotal produk tersebut109else: print([INFO])Jika tidak ditemukan, tampilkan pesan informasi bahwa produk tidak ada di keranjang

Method tampilkan_keranjang & total_harga
BarisKodePenjelasan111def tampilkan_keranjang(self):Mendefinisikan method untuk menampilkan semua produk di keranjang dalam format tabel struk belanja112–113print("KERANJANG BELANJA ANDA") ... print(header)Mencetak judul dan header kolom tabel (No, ID, Nama Produk, Harga, Qty, Subtotal)114–124for i in range(...): while current is not None:Iterasi seluruh slot dan chain hash table untuk mengumpulkan semua produk yang ada119subtotal = v['harga'] * v['jumlah']Menghitung subtotal setiap produk dengan mengalikan harga dan jumlah125–126if not ada_isi: print("(Keranjang kosong)")Jika tidak ada produk sama sekali, tampilkan pesan keranjang kosong128def total_harga(self):Mendefinisikan method untuk menghitung dan mengembalikan total harga seluruh produk di keranjan


Method checkout
BarisKodePenjelasan135def checkout(self):Mendefinisikan method untuk memproses pembayaran dan mengosongkan keranjang136–138if self.total_harga() == 0: print([INFO])Validasi: jika keranjang kosong, batalkan proses checkout139self.tampilkan_keranjang()Menampilkan struk belanja sebelum pembayaran dikonfirmasi140–141print(f"Pembayaran ... berhasil.") ...Mencetak konfirmasi pembayaran beserta total yang harus dibayar142self.hashmap.table = [None] * self.hashmap.SIZEMengosongkan seluruh slot hash table, mereset keranjang ke kondisi awal

ungsi menu() & main()
BarisKodePenjelasan145def menu():Mendefinisikan fungsi untuk menampilkan daftar pilihan menu utama program146–153print("SISTEM KERANJANG BELANJA") ...Mencetak 8 opsi menu: tambah, kurangi, hapus, cari, tampilkan, lihat hash table, checkout, keluar155def main():Fungsi utama yang menjalankan seluruh alur program secara interaktif156keranjang = KeranjangBelanja()Membuat instance keranjang belanja baru157–165katalog = {...}Mendeklarasikan dictionary katalog produk yang berisi 8 produk dengan ID, nama, dan harga166–167pilih = 0; while pilih != 8:Perulangan utama program yang terus berjalan sampai pengguna memilih menu 8 (Keluar)
168–170try: pilih = int(input(...))Membaca pilihan menu dari pengguna dan mengkonversi ke integer171except ValueError: ... continueMenangkap kesalahan jika input bukan angka, lalu kembali ke tampilan menu

















