*Judul Program*

Sistem Antrian Call Center, Implementasi Queue Array (Tugas Akhir 4.4)

Program ini merupakan implementasi struktur data Queue berbasis Array (List Python) menggunakan bahasa pemrograman Python dengan studi kasus Sistem Antrian Call Center. Program memungkinkan pengguna mendaftarkan nama pelanggan ke dalam antrean, melayani pelanggan secara berurutan, melihat pelanggan terdepan, serta menampilkan seluruh isi antrean.

Queue Array bekerja berdasarkan prinsip FIFO (First In, First Out), yaitu pelanggan yang pertama kali masuk ke antrean akan menjadi pelanggan pertama yang dilayani. Pada implementasi ini, Queue dibangun menggunakan list Python sebagai pengganti array, di mana:

- Operasi EnQueue dilakukan dengan append() yang menambahkan elemen ke bagian belakang list.
- Operasi DeQueue dilakukan dengan pop(0) yang mengambil dan menghapus elemen dari bagian depan list.

Berbeda dengan implementasi Queue berbasis Linked List yang menggunakan Node dan pointer (front_ptr, rear_ptr), Queue Array pada program ini menyimpan seluruh data secara langsung di dalam satu struktur list yang bersifat dinamis. Kompleksitas waktu operasi utamanya adalah O(1) untuk enqueue dan O(n) untuk dequeue karena seluruh elemen list digeser satu posisi ke depan setiap kali pop(0) dipanggil.

<img width="945" height="956" alt="Screenshot 2026-05-19 194504" src="https://github.com/user-attachments/assets/54fe1037-88d7-420d-995c-8d588233b9ea" />

<img width="805" height="963" alt="Screenshot 2026-05-19 194524" src="https://github.com/user-attachments/assets/f4b6dd9b-eba4-4256-9c08-862bd80fad9d" />

<img width="845" height="211" alt="Screenshot 2026-05-19 194541" src="https://github.com/user-attachments/assets/dbe69df7-746d-4729-96b0-13b43d4ed123" />

Penjelasan Logika Perbaris :

Class QueueCallCenter :
Baris 1 : class QueueCallCenter: yaitu Mendefinisikan kelas QueueCallCenter sebagai representasi struktur data Queue Array untuk sistem call center

Baris 2 : def __init__(self) yaitu Konstruktor kelas yang dijalankan otomatis saat objek dibuat

Baris 3 : self.queue = [] yaitu Mendeklarasikan list kosong queue sebagai array dinamis yang menjadi wadah penyimpanan data antrean pelanggan. Berbeda dengan Queue Linked List, tidak ada Node maupun pointer front_ptr/rear_ptr — seluruh data tersimpan langsung di dalam list ini

Method enqueue(self, nama) : 
Baris 6 : def enqueue(self, nama): yaitu Mendefinisikan method EnQueue untuk menambahkan pelanggan baru ke bagian belakang antrean, menerima parameter nama berupa string

Baris 7 : self.queue.append(nama) yaitu Menambahkan nama pelanggan ke posisi paling belakang list menggunakan method .append(). Operasi ini setara dengan menempatkan elemen di posisi rear pada Queue Array, dengan kompleksitas waktu O(1)

Baris 8 : print(f"{nama} masuk ke antrean call center.") yaitu Menampilkan konfirmasi bahwa pelanggan berhasil masuk ke antrean

Method dequeue(self) : 
Baris 11 : def dequeue(self): yaitu Mendefinisikan method DeQueue untuk melayani dan menghapus pelanggan dari bagian depan antrean

Baris 12 : if self.is_empty(): yaitu Memeriksa kondisi Queue Underflow — apakah antrean kosong sebelum melakukan operasi pop

Baris 13 : print("Tidak ada pelanggan dalam antrean.") yaitu Menampilkan pesan peringatan jika antrean kosong (kondisi Underflow), program tidak crash

Baris 15 : pelanggan = self.queue.pop(0) yaitu Mengambil dan menghapus elemen pada indeks ke-0 (posisi front) dari list. Setelah ini semua elemen tersisa digeser satu posisi ke depan oleh Python secara otomatis, sehingga kompleksitas operasi ini adalah O(n)

Baris 16 : print(f"{pelanggan} sedang dilayani.") yaitu Menampilkan nama pelanggan yang berhasil diambil dari depan antrean dan sedang dilayani

Method peek(self)  : 
Baris 19 : def peek(self): yaitu Mendefinisikan method Peek untuk melihat elemen paling depan antrean tanpa menghapusnya — hanya membaca nilai front

Baris 20 : if self.is_empty(): yaitu Memeriksa apakah antrean kosong sebelum mengakses elemen pertama

Baris 21 : print("Antrean kosong.") yaitu Menampilkan pesan jika tidak ada pelanggan dalam antrean

Baris 23 : print(f"Pelanggan berikutnya: {self.queue[0]}") yaitu Mengakses elemen pada indeks ke-0 (posisi front array) dan menampilkannya tanpa menghapus, kompleksitas O(1)

Method is_empty(self) : 
Baris 26 : def is_empty(self): yaitu Mendefinisikan method IsEmpty sebagai pengecekan kondisi kosong yang digunakan sebagai validasi oleh method-method lain

Baris 27 : return len(self.queue) == 0 yaitu Mengembalikan True jika jumlah elemen dalam list adalah 0 (antrean kosong), dan False jika masih ada elemen. Ini setara dengan pengecekan front_idx == -1 pada implementasi Queue Array berbasis indeks

Method display(self) : 
Baris 30 : def display(self): yaitu Mendefinisikan method untuk menampilkan seluruh isi antrean dari posisi front (depan) hingga rear (belakang)

Baris 31 : if self.is_empty(): yaitu Memeriksa apakah antrean kosong sebelum melakukan iterasi

Baris 32 : print("Antrean kosong.") yaitu Menampilkan pesan jika tidak ada data untuk ditampilkan

Bsris 34 : print("Daftar antrean call center:") yaitu Mencetak judul daftar antrean

Baris 35 : for i, pelanggan in enumerate(self.queue, start=1): yaitu Melakukan iterasi pada seluruh elemen list queue dari indeks 0 (front) hingga akhir (rear), dengan penomoran dimulai dari 1 menggunakan fungsi enumerate()

Baris 36 : print(f"{i}. {pelanggan}") yaitu Mencetak nomor urut dan nama pelanggan untuk setiap elemen dalam antrean

Fungsi main() :
Baris 39 : def main(): yaitu Fungsi utama yang menjalankan seluruh logika program dan interaksi pengguna

Baris 40 : call_center = QueueCallCenter() yaitu Membuat objek baru dari kelas QueueCallCenter, menginisialisasi Queue Array dengan list kosong

Baris 42 : while True: yaitu Perulangan tak terbatas agar menu terus ditampilkan hingga pengguna memilih keluar

Baris 43–48 : print("\n SISTEM CALL CENTER ") ... yaitu Mencetak header dan lima pilihan menu program ke layar

Baris 51 : pilihan = int(input("Pilih menu: ")) yaitu Membaca pilihan menu dari pengguna dan mengubahnya ke tipe integer

Baris 52-54 : except ValueError: yaitu Menangkap kesalahan jika pengguna memasukkan input yang bukan angka, lalu melanjutkan perulangan untuk meminta input ulang

Fungsi main() : 
Baris 56-58 : if pilihan == 1: yaitu Jika memilih 1, membaca nama pelanggan dari input lalu memanggil enqueue() untuk menambah ke belakang antrean

Baris 60 & 61 : elif pilihan == 2: yaitu Jika memilih 2, memanggil dequeue() untuk melayani dan menghapus pelanggan dari depan antrean

Baris 66 & 67 : elif pilihan == 3: yaitu Jika memilih 3, memanggil peek() untuk melihat pelanggan terdepan tanpa menghapusnya dari antrean

Baris 66 & 67 : elif pilihan == 4: yaitu Jika memilih 4, memanggil display() untuk menampilkan seluruh isi antrean dari depan ke belakang

69 & 70 : elif pilihan == 5: yaitu Jika memilih 5, mencetak pesan selesai dan menghentikan perulangan dengan break

Baris 73 & 74 : else: yaitu Menangani input pilihan yang tidak terdapat dalam menu (bukan angka 1–5)

Baris 77 : if __name__ == "__main__": yaitu Memastikan fungsi main() hanya dijalankan saat file dieksekusi langsung, bukan saat diimpor sebagai modul

Baris 78 : main() yaitu Memanggil fungsi utama untuk memulai program

Output : 

<img width="1410" height="731" alt="Screenshot 2026-05-19 211453" src="https://github.com/user-attachments/assets/c9c738a2-2e6b-443e-abff-538811f2f49e" />

<img width="1390" height="812" alt="Screenshot 2026-05-19 211507" src="https://github.com/user-attachments/assets/933120e9-411e-4af9-8ed7-f08da1e31383" />

<img width="1305" height="601" alt="Screenshot 2026-05-19 211520" src="https://github.com/user-attachments/assets/abc4237e-a79a-4e91-9f8f-b1f938a71aec" />

Link YouTube : https://youtu.be/fiV2uET9IIg?si=kU6KEDch5x7owRAM





