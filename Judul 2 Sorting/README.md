Judul Program

Perangkingan Skor Peserta dengan implementasi Bubble Sort Descending

Program ini merupakan implementasi algoritma Bubble Sort menggunakan bahasa pemrograman Python dengan studi kasus Perangkingan Skor Peserta. Program memungkinkan pengguna memasukkan nama dan skor sejumlah peserta, lalu mengurutkannya dari skor tertinggi ke terendah (descending) menggunakan algoritma Bubble Sort, dan menampilkan hasilnya dalam bentuk tabel peringkat.

Algoritma Bubble Sort bekerja dengan cara membandingkan dua elemen yang bersebelahan secara berulang. Pada versi descending ini, jika elemen sebelah kiri lebih kecil dari elemen sebelah kanan maka keduanya ditukar, sehingga nilai terbesar akan "menggelembung" ke posisi paling depan. Kompleksitas waktu algoritma ini adalah O(n²) pada kasus rata-rata dan terburuk.

<img width="1365" height="936" alt="Screenshot 2026-05-04 214418" src="https://github.com/user-attachments/assets/0040491c-a500-4ddd-9460-913b8a889aab" />
<img width="989" height="170" alt="Screenshot 2026-05-04 214430" src="https://github.com/user-attachments/assets/5588b85e-f896-464e-a0ad-9a1b47083794" />

Penjelasan Logika Perbari : 

Baris 1 : def bubble_sort_descending(data) yaitu Menerima list peserta yang berisi sub-list [nama, skor].  

Baris 3 : for j in range(n - i - 1) yaitu : Loop dalam untuk membandingkan elemen yang bersebelahan.  

Baris 5 : if data[j][1] < data[j + 1][1] yaitu Mengakses indeks [1] untuk membandingkan skor secara menurun (descending).  1

Baris 6 : data[j], data[j + 1] = ... yaitu Melakukan teknik Pythonic swap untuk menukar seluruh data peserta sekaligus tanpa variabel bantuan.  

11-14  : try: ... except ValueError yaitu Menangani kesalahan jika user memasukkan karakter selain angka pada input jumlah peserta.  

Baris 16  : peserta = [] yaitu Inisialisasi satu list tunggal untuk menampung seluruh pasangan nama dan skor.  

Baris 23 : peserta.append([nama, skor]) yaitu Menggabungkan nama dan skor ke dalam satu elemen agar data tetap sinkron saat disortir.  

Baris 34 : enumerate(peserta, 1) yaitu Digunakan untuk memberikan penomoran peringkat otomatis mulai dari angka 1 saat mencetak hasil.  


link YouTube : 
https://youtu.be/FYKwwtUJN_0?si=CGaj6q19WNvFRaFq
