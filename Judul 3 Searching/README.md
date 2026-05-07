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

6while l <= r:Perulangan utama pencarian; berjalan selama pointer kiri tidak melewati pointer kanan

7m = l + (r - l) // 2Menghitung indeks tengah (median) menggunakan rumus aman untuk menghindari integer overflow

8print(f"Median: {m}, nilai: {arr[m]}")Menampilkan indeks tengah dan nilai elemen pada posisi tersebut untuk menelusuri proses pencarian

10if arr[m] == target:Kondisi jika elemen tengah sama dengan nilai yang dicari (target ditemukan)

11pos = mMenyimpan indeks posisi ditemukannya target ke variabel pos

12breakMenghentikan perulangan karena target sudah ditemukan

13elif arr[m] < target:Kondisi jika elemen tengah lebih kecil dari target (target berada di bagian kanan)

14print("Mencari di kanan")Menampilkan informasi bahwa pencarian dilanjutkan ke bagian kanan

15l = m + 1Menggeser pointer kiri ke satu posisi setelah median, mempersempit area pencarian ke kanan

16else:Kondisi jika elemen tengah lebih besar dari target (target berada di bagian kiri)

17print("Mencari di kiri")Menampilkan informasi bahwa pencarian dilanjutkan ke bagian kiri

18r = m - 1Menggeser pointer kanan ke satu posisi sebelum median, mempersempit area pencarian ke kiri

20return posMengembalikan posisi indeks target jika ditemukan, atau -1 jika tidak ditemukan








