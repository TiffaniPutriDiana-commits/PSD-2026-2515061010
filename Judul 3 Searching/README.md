## Judul Program

Pencarian NPM Siswa, Implementasi Binary Search (Tugas Akhir)

Program ini merupakan implementasi algoritma Binary Search menggunakan bahasa pemrograman Python dengan studi kasus Pencarian NPM (Nomor Pokok Mahasiswa) Siswa. Program memungkinkan pengguna untuk mencari NPM tertentu dari sebuah daftar NPM yang telah terurut, lalu menampilkan posisi indeks tempat data tersebut ditemukan.

Algoritma yang diterapkan adalah Binary Search, yaitu metode pencarian yang bekerja pada data terurut dengan membagi rentang pencarian menjadi dua bagian setiap iterasi. Program menggunakan dua pointer l (left/kiri) dan r (right/kanan) serta nilai tengah m (median) yang dihitung dengan rumus l + (r - l) // 2 untuk menghindari overflow. Setiap langkah pencarian ditampilkan ke layar sehingga proses dapat dipantau secara transparan. Program juga dilengkapi dengan validasi input untuk memastikan pengguna memasukkan data berupa angka yang valid.

<img width="933" height="545" alt="Screenshot 2026-05-07 092955" src="https://github.com/user-attachments/assets/e53ecf6c-88f7-4776-b691-cd9e29d23176" />
<img width="1045" height="622" alt="Screenshot 2026-05-07 092659" src="https://github.com/user-attachments/assets/4f271ccb-b9cc-4ffa-9265-97f35a033a2a" />

Penjelasan Logika Perbaris : 


Fungsi binary_search(arr, n, target)

Baris 1 : def binary_search(arr, n, target) yaitu Mendefinisikan fungsi binary search dengan parameter: arr (array data), n (jumlah elemen), dan target (nilai yang dicari)

Baris 2 : l = 0 yaitu Menginisialisasi pointer kiri l pada indeks pertama array (indeks 0)

Baris 3 : r = n - 1 yaitu Menginisialisasi pointer kanan r pada indeks terakhir array

Baris 4 : pos = -1 yaitu Menginisialisasi variabel pos dengan nilai -1 sebagai tanda bahwa data belum ditemukan

Baris 6 : while l <= r yaitu Perulangan utama pencarian; berjalan selama pointer kiri tidak melewati pointer kanan

Baris 7 : m = l + (r - l) // 2 yaitu Menghitung indeks tengah (median) menggunakan rumus aman untuk menghindari integer overflow

Baris 8 : print(f"Median: {m}, nilai: {arr[m]}") yaitu Menampilkan indeks tengah dan nilai elemen pada posisi tersebut untuk menelusuri proses pencarian

Baris 10 : if arr[m] == target: yaitu Kondisi jika elemen tengah sama dengan nilai yang dicari (target ditemukan)

Baris 11 : pos = m yaitu Menyimpan indeks posisi ditemukannya target ke variabel pos

Baris 12 : break yaitu Menghentikan perulangan karena target sudah ditemukan

Baris 13 : elif arr[m] < target: yaitu Kondisi jika elemen tengah lebih kecil dari target (target berada di bagian kanan)

Baris 14 : print("Mencari di kanan") yaitu Menampilkan informasi bahwa pencarian dilanjutkan ke bagian kanan

Baris 15 : l = m + 1 yaitu Menggeser pointer kiri ke satu posisi setelah median, mempersempit area pencarian ke kanan

Baris 16 : else: yaitu Kondisi jika elemen tengah lebih besar dari target (target berada di bagian kiri)

Baris 17 : print("Mencari di kiri") yaitu Menampilkan informasi bahwa pencarian dilanjutkan ke bagian kiri

Baris 18 : r = m - 1 yaitu Menggeser pointer kanan ke satu posisi sebelum median, mempersempit area pencarian ke kiri

Baris 20 : return pos yaitu Mengembalikan posisi indeks target jika ditemukan, atau -1 jika tidak ditemukan


Fungsi main()
Baris 23 : def main(): yaitu Fungsi utama yang menjalankan seluruh logika program

Baris 24 : arr = [2515061101, ...] yaitu Mendeklarasikan array berisi 6 NPM siswa yang sudah terurut secara menaik — syarat wajib agar Binary Search dapat bekerja dengan benar

Baris 25 : n = len(arr) yaitu Menghitung jumlah elemen pada array dan menyimpannya ke variabel n

Baris 27 : print("Data NPM siswa:", arr) yaitu Menampilkan seluruh isi array NPM ke layar sebagai informasi awal kepada pengguna

Baris 29 : while True: yaitu Perulangan validasi input yang akan terus berulang hingga pengguna memasukkan angka yang valid

Baris 30 : try: yaitu Blok percobaan untuk menangkap potensi kesalahan saat konversi input

Baris 31 : target = int(input("Masukkan NPM yang dicari: ")) yaitu Membaca NPM yang ingin dicari dari pengguna dan mengkonversinya ke tipe integer

Baris 32 : break yaitu Keluar dari perulangan validasi jika input berhasil dikonversi

Baris 33 : except ValueError: yaitu Menangkap kesalahan jika input bukan angka

Baris 34 : print("Input tidak valid!") yaitu Menampilkan pesan kesalahan dan meminta pengguna mengulang input

Baris 36 : pos = binary_search(arr, n, target) yaitu Memanggil fungsi binary search dan menyimpan hasil posisi ke variabel pos

Baris 38 : if pos != -1: yaitu Kondisi jika pos bukan -1, berarti data ditemukan

Baris 39 : print(f"Data ditemukan pada indeks ke-{pos}") yaitu Menampilkan indeks posisi data yang ditemukan

Baris 40 : else: yaitu Kondisi jika pos bernilai -1, berarti data tidak ada dalam array

Baris 41 : print("Data tidak ditemukan") yaitu Menampilkan pesan bahwa data yang dicari tidak ada

Baris 44 : if __name__ == "__main__": yaitu Memastikan fungsi main() hanya dijalankan ketika file ini dieksekusi langsung, bukan saat diimpor sebagai modul

Baris 45 : main() yaitu Memanggil fungsi utama untuk memulai program









