Judul Program
Daftar Harga Barang 

Implementasi List 1 Dimensi (Tugas Akhir 1.4)

Deskripsi Singkat
Program ini merupakan implementasi struktur data List 1 Dimensi menggunakan bahasa pemrograman Python dengan studi kasus Daftar Harga Barang Kebutuhan Pokok. Program memungkinkan pengguna untuk memasukkan harga dari 5 jenis barang (Beras, Gula, Minyak, Tepung, dan Garam), lalu menampilkannya dalam format mata uang Rupiah yang sesuai standar penulisan Indonesia.

Algoritma yang diterapkan adalah penyimpanan data secara sekuensial menggunakan List 1 Dimensi (harga = [0] * 5), di mana setiap elemen diakses menggunakan indeks tunggal mulai dari 0 hingga 4. Program dilengkapi dengan menu interaktif, validasi input, dan fungsi formatting Rupiah untuk memastikan data tampil dengan benar dan rapi.
<img width="1107" height="557" alt="Screenshot 2026-04-29 132127" src="https://github.com/user-attachments/assets/3376da58-b84d-4a40-a67d-54023709e4dd" />
<img width="974" height="662" alt="Screenshot 2026-04-29 132205" src="https://github.com/user-attachments/assets/75499df8-6556-4e1d-891a-24b91913ac2b" />

penjelasan logika perbaris :

Baris 1 : def format_rupiah(angka) yaitu Mendefinisikan fungsi untuk mengubah angka menjadi format mata uang Rupiah

Baris 2 : hasil = f"{angka:,}".replace(",", ".") yaitu Memformat angka dengan pemisah ribuan menggunakan koma (15,000), lalu mengganti koma dengan titik sesuai format Indonesia (15.000)

Baris 3 : return f"Rp {hasil},-" yaitu Mengembalikan string lengkap format Rupiah, contoh: Rp 15.000,-

Baris 5 : def menu(): yaitu Mendefinisikan fungsi untuk menampilkan menu utama program

Baris 6-9 : print(...) yaitu Mencetak judul dan pilihan menu ke layar (menu 1, 2, dan 3)

Baris 11 : def main(): yaitu Fungsi utama yang menjalankan seluruh logika program

Baris 12 : nama_barang = ["Beras", "Gula", "Minyak", "Tepung", "Garam"] yaitu Mendeklarasikan List 1 Dimensi berisi 5 nama barang kebutuhan pokok

Baris 13 : harga = [0] * 5 yaitu Mendeklarasikan List 1 Dimensi dengan 5 elemen, seluruhnya diisi nilai awal 0. Ini adalah inti dari implementasi List 1D

Baris 15 : running = True yaitu Variabel kontrol loop agar program terus berjalan selama belum keluar

Baris 16 : while running:Perulangan utama program, berjalan terus selama running bernilai True

Baris 17 : menu()Memanggil fungsi menu() untuk menampilkan pilihan menu setiap iterasi

Baris 18-22 : try / except ValueError yaitu Blok validasi input: jika pengguna memasukkan bukan angka, program tidak crash melainkan meminta input ulang

Baris 19: choice = int(input("Pilihan: ")) yaitu Membaca pilihan menu dari pengguna dan mengubahnya ke tipe integer

Baris 24 : if choice == 1: yaitu Kondisi jika pengguna memilih menu 1

Baris 25 : print(...) yaitu Mencetak header tabel (judul kolom dan garis pemisah)

Baris 26 : for i in range(5): yaitu Perulangan sebanyak 5 kali untuk mengisi setiap elemen list harga

Baris 27 : while True: yaitu Perulangan validasi agar input diulang jika tidak valid

Baris 29 : harga[i] = int(input(...))Menyimpan nilai harga yang diinput ke elemen list pada indeks i. Inilah cara akses dan pengisian List 1D menggunakan indeks

Baris 30 : break yaitu Keluar dari loop validasi jika input berhasil

Baris 31 : except ValueError yaitu Menangkap kesalahan jika input bukan angka, lalu meminta input ulang

Baris 35 : elif choice == 2: yaitu Kondisi jika pengguna memilih menu 2

Baris 36 : print(...) yaitu Mencetak header tabel (judul kolom dan garis pemisah)

Baris 37 : for i in range(5): yaitu Perulangan untuk menampilkan seluruh isi list harga dari indeks 0 hingga 4

Baris 38 : print(f"{i+1}. {nama_barang[i]:<12} {format_rupiah(harga[i])}") yaitu Mencetak nomor urut, nama barang (rata kiri 12 karakter), dan harga dalam format Rupiah. nama_barang[i] dan harga[i] adalah akses elemen List 1D menggunakan indeks

Baris 40 : elif choice == 3: yaitu Kondisi jika pengguna memilih menu 3

Baris 41 : running = False yaitu Mengubah nilai running menjadi False sehingga perulangan while berhenti

Baris 42 : print("Program selesai.") yaitu Mencetak pesan bahwa program telah berakhir

Baris 44 : else: yaitu Kondisi yang dijalankan jika pengguna memasukkan angka selain 1, 2, dan 3.

Baris 45 : print("Pilihan tidak valid!") yaitu Mencetak pesan peringatan bahwa input tidak sesuai pilihan menu, lalu program kembali menampilkan menu dari awal.

Baris 47 : if __name__ == "__main__": yaitu Memastikan fungsi main() hanya dijalankan ketika file ini dieksekusi langsung, bukan saat diimpor sebagai modul

Baris 48 : main() yaitu Memanggil fungsi utama untuk memulai program


Output Program 

Tampilan menu :
<img width="519" height="304" alt="Screenshot 2026-04-28 120614" src="https://github.com/user-attachments/assets/0d936bfb-b25b-4477-b8a5-6bfe57ace161" />

Tampilan saat memasuka harga (Menu 1):
<img width="472" height="192" alt="Screenshot 2026-04-28 120748" src="https://github.com/user-attachments/assets/7a9395a6-0a83-4e71-b286-3e891c6b227a" />

Tampilan saat memasuka harga (Menu 2):
<img width="492" height="193" alt="Screenshot 2026-04-28 120805" src="https://github.com/user-attachments/assets/189715f9-2bc6-4c8c-9ef4-281815ae9573" />

Tampilan saat menu 3 :
<img width="539" height="164" alt="Screenshot 2026-04-28 120818" src="https://github.com/user-attachments/assets/d4ed88b0-80f6-46da-b62a-2900043f8f92" />





Link YouTube
https://youtu.be/pnOdRSRm9Q0?si=XFHc6MEAZ3pLR4Gp
