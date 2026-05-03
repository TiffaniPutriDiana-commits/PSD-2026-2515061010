Judul Program

Perangkingan Skor Peserta 

Implementasi Bubble Sort Descending

Program ini merupakan implementasi algoritma Bubble Sort menggunakan bahasa pemrograman Python dengan studi kasus Perangkingan Skor Peserta. Program memungkinkan pengguna memasukkan nama dan skor sejumlah peserta, lalu mengurutkannya dari skor tertinggi ke terendah (descending) menggunakan algoritma Bubble Sort, dan menampilkan hasilnya dalam bentuk tabel peringkat.

Algoritma Bubble Sort bekerja dengan cara membandingkan dua elemen yang bersebelahan secara berulang. Pada versi descending ini, jika elemen sebelah kiri lebih kecil dari elemen sebelah kanan maka keduanya ditukar, sehingga nilai terbesar akan "menggelembung" ke posisi paling depan. Kompleksitas waktu algoritma ini adalah O(n²) pada kasus rata-rata dan terburuk.

<img width="1025" height="901" alt="Screenshot 2026-05-03 114242" src="https://github.com/user-attachments/assets/586e2154-836f-4280-af23-617b03a08c60" />


Penjelasan Logika Perbaris : 

Baris 1 : def tukar(arr, i, j) yaitu Mendefinisikan fungsi untuk menukar dua elemen dalam list berdasarkan indeks i dan j

Baris 2 : temp = arr[i] yaitu Menyimpan nilai elemen indeks i ke variabel sementara temp agar tidak hilang saat ditukar

Baris 3 : arr[i] = arr[j] yaitu Mengisi posisi indeks i dengan nilai dari indeks j

Baris 4 : arr[j] = temp yaiutu Mengisi posisi indeks j dengan nilai temp (nilai asli indeks i), sehingga pertukaran selesai

Baris 6 : def bubble_sort_descending(arr, n) yaitu Mendefinisikan fungsi pengurutan Bubble Sort secara menurun (descending)

Baris 7 : for i in range(n - 1) yaitu Perulangan luar sebanyak n-1 kali, mewakili setiap babak pengurutan. Setiap babak memastikan satu elemen terbesar sudah berada di posisi yang benar  

Baris 8 : for j in range(n - i - 1) yaitu Perulangan dalam untuk membandingkan elemen bersebelahan. Semakin bertambah i, semakin sedikit elemen yang perlu dibandingkan karena elemen di ujung kiri sudah terurut

Baris 9 : if arr[j] < arr[j + 1] yaituMembandingkan elemen saat ini dengan elemen sebelahnya. Jika elemen kiri lebih kecil dari kanan, artinya urutan salah untuk descending sehingga perlu ditukar

Baris 10 : tukar(arr, j, j + 1) yaitu Memanggil fungsi tukar() untuk menukar posisi elemen j dan j+1

Baris 12 : def main(): yaitu Fungsi utama yang menjalankan seluruh logika program

Baris 13 : n = int(input("Masukkan jumlah peserta: ")) yaitu Membaca jumlah peserta dari pengguna dan mengubahnya ke tipe integer

Baris 15 : nama = [] yaitu Mendeklarasikan list kosong untuk menyimpan nama seluruh peserta

Baris 16 : skor = [] yaitu Mendeklarasikan list kosong untuk menyimpan skor seluruh peserta

Baris 18 : for i in range(n): yaitu Perulangan sebanyak n kali untuk memasukkan data setiap peserta

Baris 19 : print(f"\nPeserta ke-{i+1}") yaitu Mencetak label urutan peserta yang sedang diinput (dimulai dari 1)

Baris 20 : nama.append(input("Nama  : ")) yaitu Membaca nama peserta dan menambahkannya ke list nama menggunakan .append()

Baris 21 : skor.append(int(input("Skor  : "))) yaitu Membaca skor peserta, mengubahnya ke integer, lalu menambahkannya ke list skor

Baris 24 : print(f"\nData sebelum diurutkan: {skor}") yaitu Menampilkan isi list skor sebelum proses pengurutan dilakukan

Baris 26 : bubble_sort_descending(skor, n) yaitu Memanggil fungsi Bubble Sort untuk mengurutkan list skor secara descending

Baris 27 : print("Data setelah diurutkan ...") yaitu Mencetak keterangan bahwa data sudah diurutkan

Baris 28 : print(f"\n{'No':<5} {'Nama':<20} {'Skor':>6}") yaitu Mencetak header tabel dengan format rata kiri untuk No dan Nama, rata kanan untuk Skor

Baris 29 : for i in range(n): yaitu Perulangan untuk menampilkan seluruh data peserta setelah diurutkan

Baris 30 : print(f"{i+1:<5} {nama[i]:<20} {skor[i]:>6}") yaitu Mencetak nomor peringkat, nama peserta, dan skor dalam format tabel yang rapi

Baris 32 : if __name__ == "__main__": yaitu Memastikan fungsi main() hanya dijalankan saat file dieksekusi langsung, bukan saat diimpor sebagai modul

Baris 33 : main() yaitu Memanggil fungsi utama untuk memulai program

Output : 

<img width="1538" height="659" alt="Screenshot 2026-05-03 151845" src="https://github.com/user-attachments/assets/5a9a256d-6f8e-47f0-9493-5c89f638a40b" />


Link YouTube : 
https://youtu.be/xrgK64ErSzQ?si=fK6sWCR5ZP8jkcyg







