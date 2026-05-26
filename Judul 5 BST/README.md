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
BarisKodePenjelasan1class Node:Mendefinisikan kelas Node yang merepresentasikan satu simpul (node) dalam pohon BST2def __init__(self, key):Konstruktor kelas Node yang menerima parameter key sebagai nilai yang disimpan3self.key = keyMenyimpan nilai data node ke atribut key4self.left = NoneMenginisialisasi pointer anak kiri dengan None (belum memiliki anak kiri)5self.right = NoneMenginisialisasi pointer anak kanan dengan None (belum memiliki anak kanan)


Class BSTDasar — Konstruktor & Fungsi insert_node
BarisKodePenjelasan7class BSTDasar:Mendefinisikan kelas utama yang berisi seluruh operasi BST8def __init__(self):Konstruktor kelas BSTDasar9self.root = NoneMenginisialisasi akar pohon dengan None, menandakan pohon masih kosong11def insert_node(self, root, key):Fungsi rekursif untuk menyisipkan nilai baru ke posisi yang tepat dalam BST12if root is None:Kondisi dasar rekursi: jika posisi kosong, buat node baru di sini13return Node(key)Membuat dan mengembalikan node baru dengan nilai key14if key < root.key:Jika nilai baru lebih kecil dari node saat ini, masuk ke subtree kiri15root.left = self.insert_node(root.left, key)Rekursif ke subtree kiri dan sambungkan hasilnya ke root.left16elif key > root.key:Jika nilai baru lebih besar dari node saat ini, masuk ke subtree kanan17root.right = self.insert_node(root.right, key)Rekursif ke subtree kanan dan sambungkan hasilnya ke root.right18return rootMengembalikan node saat ini (tidak ada perubahan jika nilai sudah ada)


Fungsi insert & search_node
BarisKodePenjelasan20def insert(self, key):Fungsi publik untuk menyisipkan nilai; memanggil insert_node mulai dari akar21self.root = self.insert_node(self.root, key)Memperbarui akar pohon dengan hasil penyisipan rekursif23def search_node(self, root, key):Fungsi rekursif untuk mencari nilai tertentu dalam BST24if root is None: return FalseKondisi dasar: jika node tidak ditemukan hingga ujung pohon, kembalikan False25if root.key == key: return TrueNilai ditemukan pada node saat ini, kembalikan True26–27if key < root.key:Jika nilai yang dicari lebih kecil, lanjutkan pencarian ke subtree kiri28return self.search_node(root.right, key)Jika tidak lebih kecil, lanjutkan pencarian ke subtree kanan


Fungsi Traversal — inorder, preorder, postorder
BarisKodePenjelasan31def inorder(self, root):Mendefinisikan traversal Inorder: Kiri → Root → Kanan (menghasilkan urutan naik)32if root is None: returnKondisi dasar rekursi: hentikan jika node kosong33self.inorder(root.left)Kunjungi seluruh subtree kiri terlebih dahulu34print(root.key, end=" ")Cetak nilai node saat ini35self.inorder(root.right)Kunjungi seluruh subtree kanan37def preorder(self, root):Mendefinisikan traversal Preorder: Root → Kiri → Kanan40print(root.key, end=" ")Cetak nilai node saat ini terlebih dahulu sebelum ke anak-anaknya44def postorder(self, root):Mendefinisikan traversal Postorder: Kiri → Kanan → Root47print(root.key, end=" ")Cetak nilai node saat ini setelah kedua subtree selesai dikunjungi


Fungsi find_min & find_max
BarisKodePenjelasan49def find_min(self, root):Fungsi untuk menemukan nilai terkecil dalam BST50if root is None: return -1Jika pohon kosong, kembalikan -1 sebagai tanda tidak ada data51current = rootMulai dari akar pohon52while current.left is not None:Terus bergerak ke kiri selama masih ada anak kiri53current = current.leftPindah ke node anak kiri54return current.keyNode paling kiri adalah nilai terkecil dalam BST56def find_max(self, root):Fungsi untuk menemukan nilai terbesar dalam BST59while current.right is not None:Terus bergerak ke kanan selama masih ada anak kanan61return current.keyNode paling kanan adalah nilai terbesar dalam BST


Fungsi count_nodes & sum_nodes
BarisKodePenjelasan63def count_nodes(self, root):Fungsi rekursif untuk menghitung total jumlah node dalam pohon64if root is None: return 0Kondisi dasar: node kosong berkontribusi 065return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)Hitung node saat ini (1) ditambah jumlah node di subtree kiri dan kanan67def sum_nodes(self, root):Fungsi rekursif untuk menjumlahkan seluruh nilai dalam pohon68if root is None: return 0Kondisi dasar: node kosong berkontribusi 069return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)Jumlahkan nilai node saat ini dengan seluruh nilai di subtree kiri dan kanan


Fungsi main() — Inisialisasi & Menu Utama
BarisKodePenjelasan72def main():Fungsi utama yang menjalankan seluruh logika program73bst = BSTDasar()Membuat objek BST baru yang masih kosong75pilih = 0Inisialisasi variabel pilihan menu76while pilih != 10:Loop utama program; berjalan terus hingga pengguna memilih opsi 10 (Keluar)77–86print(...)Mencetak tampilan menu utama dengan 10 pilihan operasi BST88–91try: pilih = int(input(...))Membaca pilihan menu dari pengguna dan mengubahnya ke integer, dengan penanganan kesalahan input


Fungsi main() — Penanganan Setiap Menu
BarisKodePenjelasan93–97if pilih == 1:Menangani menu "Masukkan nilai": membaca integer dan memasukkannya ke BST via bst.insert()99–105elif pilih == 2:Menangani menu "Cari nilai": mencari nilai di BST via bst.search() dan menampilkan hasilnya107–109elif pilih == 3:Menampilkan traversal Inorder (nilai terurut dari kecil ke besar)111–113elif pilih == 4:Menampilkan traversal Preorder115–117elif pilih == 5:Menampilkan traversal Postorder119elif pilih == 6:Memanggil find_min() dan mencetak nilai terendah dalam BST121elif pilih == 7:Memanggil find_max() dan mencetak nilai tertinggi dalam BST123elif pilih == 8:Memanggil count_nodes() dan mencetak jumlah total siswa (node)125elif pilih == 9:Memanggil sum_nodes() dan mencetak total nilai seluruh siswa127–128elif pilih == 10:Mencetak pesan "Program selesai" dan loop berakhir karena kondisi pilih != 10 tidak terpenuhi

Blok Utama
BarisKodePenjelasan131if __name__ == "__main__":Memastikan fungsi main() hanya dijalankan saat file dieksekusi langsung, bukan saat diimpor sebagai modul132main()Memanggil fungsi utama untuk memulai program

