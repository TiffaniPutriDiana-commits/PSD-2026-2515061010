**Judul Program**

BST Manajeman Nilai Ujian Siswa 

Implementasi Binary Search Tree

Program ini merupakan implementasi struktur data Binary Search Tree (BST) menggunakan bahasa pemrograman Python dengan studi kasus Manajemen Nilai Ujian Siswa. Program memungkinkan pengguna memasukkan nilai ujian, melakukan pencarian nilai, menampilkan nilai dalam berbagai urutan traversal, serta menghitung statistik seperti nilai terendah, tertinggi, jumlah siswa, dan total nilai.

Binary Search Tree (BST) adalah struktur data pohon di mana setiap node memiliki paling banyak dua anak. Node anak kiri selalu memiliki nilai lebih kecil dari node induk, sedangkan node anak kanan selalu memiliki nilai lebih besar. Struktur ini memungkinkan operasi pencarian, penyisipan, dan traversal yang efisien dengan kompleksitas waktu rata-rata O(log n).

Program menyediakan tiga jenis traversal:
-Inorder (Kiri → Root → Kanan): menghasilkan data terurut dari kecil ke besar
-Preorder (Root → Kiri → Kanan): digunakan untuk menyalin struktur pohon
-Postorder (Kiri → Kanan → Root): digunakan untuk menghapus pohon

<img width="1673" height="835" alt="Screenshot 2026-05-26 172539" src="https://github.com/user-attachments/assets/a770a26d-dbaf-496b-a610-e793f5b8de9b" />
<img width="1420" height="716" alt="Screenshot 2026-05-26 172614" src="https://github.com/user-attachments/assets/63269ad8-209f-40b1-bbc0-1130976cfc08" />
<img width="1292" height="844" alt="Screenshot 2026-05-26 172639" src="https://github.com/user-attachments/assets/7c579c02-3f6e-47f6-9c0d-251d37f9777a" />
<img width="1215" height="837" alt="Screenshot 2026-05-26 172703" src="https://github.com/user-attachments/assets/fbecb227-33b4-4a71-8c1b-890f03948d46" />
<img width="1165" height="655" alt="Screenshot 2026-05-26 172717" src="https://github.com/user-attachments/assets/9b7c4e6d-f405-46fc-8a8d-ed37dc35785d" />

Penjelasan Logika Perbaris : 

Class Node
Baris 1 : class Node: yaitu Mendefinisikan kelas Node yang merepresentasikan satu simpul (node) dalam pohon BST

Baris 2 : def __init__(self, key): yaitu Konstruktor kelas Node yang menerima parameter key sebagai nilai yang disimpan

Baris 3 : self.key = key yaitu Menyimpan nilai data node ke atribut key

Baris 4 : self.left = None yaitu Menginisialisasi pointer anak kiri dengan None (belum memiliki anak kiri) 

Baris 5 : self.right = None yaitu Menginisialisasi pointer anak kanan dengan None (belum memiliki anak kanan)


Class BSTDasar — Konstruktor & Fungsi insert_node
Baris 8 : class BSTDasar: yaitu Mendefinisikan kelas utama yang berisi seluruh operasi BST

Baris 9 : def __init__(self): yaitu Konstruktor kelas BSTDasar

Baris 10 : self.root = None yaitu Menginisialisasi akar pohon dengan None, menandakan pohon masih kosong

Baris 12 : def insert_node(self, root, key): yaitu Fungsi rekursif untuk menyisipkan nilai baru ke posisi yang tepat dalam BST

Baris 13 : if root is None: yaitu Kondisi dasar rekursi: jika posisi kosong, buat node baru di sini

Baris 14 : return Node(key) yaitu Membuat dan mengembalikan node baru dengan nilai key

Baris 15 : if key < root.key: yaitu Jika nilai baru lebih kecil dari node saat ini, masuk ke subtree kiri

Baris 16 : root.left = self.insert_node(root.left, key) yaitu Rekursif ke subtree kiri dan sambungkan hasilnya ke root.left

Baris 17 : lif key > root.key: yaitu Jika nilai baru lebih besar dari node saat ini, masuk ke subtree kanan

Baris 18 : root.right = self.insert_node(root.right, key) yaitu Rekursif ke subtree kanan dan sambungkan hasilnya ke root.right

Baris 19 : return root yaitu Mengembalikan node saat ini (tidak ada perubahan jika nilai sudah ada)


Fungsi insert & search_node
Baris 21 : def insert(self, key): yaitu Fungsi publik untuk menyisipkan nilai; memanggil insert_node mulai dari akar

Baris 22 : self.root = self.insert_node(self.root, key) yaitu Memperbarui akar pohon dengan hasil penyisipan rekursif

Baris 24 : def search_node(self, root, key): yaitu Fungsi rekursif untuk mencari nilai tertentu dalam BST

Baris 25 dan 26 : if root is None: return False yaitu Kondisi dasar: jika node tidak ditemukan hingga ujung pohon, kembalikan False

Baris 27 dan 28 : if root.key == key: return True yaitu Nilai ditemukan pada node saat ini, kembalikan True

Baris 29-30 : if key < root.key: yaitu Jika nilai yang dicari lebih kecil, lanjutkan pencarian ke subtree kiri

Baris 31 : return self.search_node(root.right, key) yaitu Jika tidak lebih kecil, lanjutkan pencarian ke subtree kanan

Baris 33 : def search(self, key): yaitu Mendefinisikan fungsi search yang menerima satu input yaitu key (nilai yang dicari).

Baris 34 : return self.search_node(self.root, key) yaitu Memanggil fungsi search_node mulai dari akar pohon (self.root), lalu langsung mengembalikan hasilnya True jika nilai ditemukan, False jika tidak.


Fungsi Traversal — inorder, preorder, postorder

Baris 36 : def inorder(self, root): yaitu Mendefinisikan traversal Inorder: Kiri → Root → Kanan (menghasilkan urutan naik)

Baris 37 & 38 : if root is None: return yaitu Kondisi dasar rekursi: hentikan jika node kosong

Baris 39 : self.inorder(root.left) yaitu Kunjungi seluruh subtree kiri terlebih dahulu

Baris 40 : print(root.key, end=" ") yaitu Cetak nilai node saat ini

Baris 41 : self.inorder(root.right) yaitu Kunjungi seluruh subtree kanan

Baris 43 : def preorder(self, root): yaitu Mendefinisikan traversal Preorder: Root → Kiri → Kanan

Baris 44 & 45 : if root is None: return yaitu Kondisi dasar rekursi: hentikan jika node kosong

Baris 46 : print(root.key, end=" ") yaitu Cetak nilai node saat ini terlebih dahulu sebelum ke anak-anaknya

Baris 47 : self.preorder(root.left) yaitu Memanggil fungsi preorder lagi secara rekursif, tapi kali ini masuk ke anak kiri dari node saat ini.

Baris 48 : self.preorder(root.right) Setelah seluruh subtree kiri selesai dikunjungi, barulah masuk ke anak kanan dari node saat ini secara rekursif.

Baris 50 : def postorder(self, root): yaitu Mendefinisikan traversal Postorder: Kiri → Kanan → Root

Baris 51 & 52 : if root is None: return yaitu Kondisi dasar rekursi: hentikan jika node kosong

Baris 53 : self.postorder(root.left) yaitu Memanggil fungsi postorder secara rekursif ke anak kiri, telusuri seluruh subtree kiri sampai habis dulu.

Baris 54 : self.postorder(root.right) yaitu Setelah subtree kiri selesai, baru telusuri anak kanan secara rekursif sampai habis.

Baris 55 : print(root.key, end=" ") yaitu Cetak nilai node saat ini setelah kedua subtree selesai dikunjungi


Fungsi find_min & find_max
Baris 57 : def find_min(self, root): yaitu Fungsi untuk menemukan nilai terkecil dalam BST

Baris 58 & 59 : if root is None: return -1 yaitu Jika pohon kosong, kembalikan -1 sebagai tanda tidak ada data

Baris 60 : current = root yaitu Mulai dari akar pohon

Baris 61 : while current.left is not None: yaitu Terus bergerak ke kiri selama masih ada anak kiri

Baris 62 : current = current.left yaitu Pindah ke node anak kiri

Baris 63 : return current.key yaitu Node paling kiri adalah nilai terkecil dalam BST

Baris 65 : def find_max(self, root): yaitu Fungsi untuk menemukan nilai terbesar dalam BST

Baris 66 & 67 : if root is None: return -1 yaitu Jika pohon kosong, kembalikan -1 sebagai tanda tidak ada data

Baris 68 : current = root yaitu Mulai dari akar pohon 

Baris 69 : while current.right is not None: yaitu Terus bergerak ke kanan selama masih ada anak kanan

Baris  71 : return current.key yaitu Node paling kanan adalah nilai terbesar dalam BST


Fungsi count_nodes & sum_nodes
Baris 73 : def count_nodes(self, root): yaitu  Fungsi rekursif untuk menghitung total jumlah node dalam pohon

Baris 74 & 75 :  if root is None: return 0 yaitu Kondisi dasar: node kosong berkontribusi 0

Baris 76 : return 1 + self.count_nodes(root.left) + self.count_nodes(root.right) yaitu Hitung node saat ini (1) ditambah jumlah node di subtree kiri dan kanan

Baris 78 : def sum_nodes(self, root): yaitu Fungsi rekursif untuk menjumlahkan seluruh nilai dalam pohon

Baris 79-80 : if root is None: return 0 yaitu Kondisi dasar: node kosong berkontribusi 0

Baris 81 : return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right) yaitu Jumlahkan nilai node saat ini dengan seluruh nilai di subtree kiri dan kanan


Fungsi main() — Inisialisasi & Menu Utama
Baris 84 : def main(): yaitu Fungsi utama yang menjalankan seluruh logika program

Baris 85 bst = BSTDasar() yaitu Membuat objek BST baru yang masih kosong

Baris 87 : pilih = 0 yaitu Inisialisasi variabel pilihan menu

Baris 88 : while pilih != 10: yaitu Loop utama program; berjalan terus hingga pengguna memilih opsi 10 (Keluar)

Baris 89-99 : print(...) yaitu Mencetak tampilan menu utama dengan 10 pilihan operasi BST

Baris 101-102 : try: pilih = int(input(...)) yaitu Membaca pilihan menu dari pengguna dan mengubahnya ke integer, dengan penanganan kesalahan input

except ValueError:
print("Input tidak valid!")
continue

Fungsi main() — Penanganan Setiap Menu
baris  107-113 : if pilih == 1: yaitu Menangani menu "Masukkan nilai": membaca integer dan memasukkannya ke BST via bst.insert()

115-122 : elif pilih == 2: yaitu Menangani menu "Cari nilai": mencari nilai di BST via bst.search() dan menampilkan hasilnya

Baris 125-128 : elif pilih == 3: yaitu Menampilkan traversal Inorder (nilai terurut dari kecil ke besar)

Baris 130-133 : elif pilih == 4: yaitu Menampilkan traversal Preorder

Baris 135-138 : elif pilih == 5: yaitu Menampilkan traversal Postorder

Baris 140-141 : elif pilih == 6: yaitu Memanggil find_min() dan mencetak nilai terendah dalam BST

Baris 143-144 : elif pilih == 7: yaitu Memanggil find_max() dan mencetak nilai tertinggi dalam BST

Baris 146-147 : elif pilih == 8: yaitu Memanggil count_nodes() dan mencetak jumlah total siswa (node)

Baris 149-150 : elif pilih == 9: yaitu Memanggil sum_nodes() dan mencetak total nilai seluruh siswa

Baris 152-153 : elif pilih == 10: yaitu Mencetak pesan "Program selesai" dan loop berakhir karena kondisi pilih != 10 tidak terpenuhi

Baris 155-156 : else: print("Pilihan tidak valid!") yaitu jika angka yang dimasukan tidak sesuai dengan menu

Baris 159 : if __name__ == "__main__": yaitu Memastikan fungsi main() hanya dijalankan saat file dieksekusi langsung, bukan saat diimpor sebagai modul

Baris 160 : main() yaitu Memanggil fungsi utama untuk memulai program

Output : 

<img width="1013" height="764" alt="Screenshot 2026-05-26 234955" src="https://github.com/user-attachments/assets/5f3907fa-08b7-44f4-b2f8-0f2f0f15524f" />
<img width="715" height="670" alt="Screenshot 2026-05-26 235005" src="https://github.com/user-attachments/assets/70f7cf47-8193-444c-b00d-1f1d3dc1abe4" />
<img width="1179" height="950" alt="Screenshot 2026-05-26 235015" src="https://github.com/user-attachments/assets/b67f8d41-29dc-48ec-bb86-04ea031641b6" />
<img width="807" height="941" alt="Screenshot 2026-05-26 235030" src="https://github.com/user-attachments/assets/a0eda758-bec6-45c1-b8e1-a3ac46b6620b" />
<img width="485" height="631" alt="Screenshot 2026-05-26 235036" src="https://github.com/user-attachments/assets/f1d76edb-7978-417c-abb4-1357d692871a" />

Link Youtube : https://youtu.be/3cmlbaqumYk?si=wS1AAB4mHZpFETOT


