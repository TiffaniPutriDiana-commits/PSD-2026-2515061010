class QueueCallCenter:
    def __init__(self):
        self.queue = []

    # Menambahkan pelanggan ke antrean
    def enqueue(self, nama):
        self.queue.append(nama)
        print(f"{nama} masuk ke antrean call center.")

    # Melayani pelanggan pertama
    def dequeue(self):
        if self.is_empty():
            print("Tidak ada pelanggan dalam antrean.")
        else:
            pelanggan = self.queue.pop(0)
            print(f"{pelanggan} sedang dilayani.")

    # Melihat pelanggan paling depan
    def peek(self):
        if self.is_empty():
            print("Antrean kosong.")
        else:
            print(f"Pelanggan berikutnya: {self.queue[0]}")

    # Mengecek apakah antrean kosong
    def is_empty(self):
        return len(self.queue) == 0

    # Menampilkan seluruh antrean
    def display(self):
        if self.is_empty():
            print("Antrean kosong.")
        else:
            print("Daftar antrean call center:")
            for i, pelanggan in enumerate(self.queue, start=1):
                print(f"{i}. {pelanggan}")


def main():
    call_center = QueueCallCenter()

    while True:
        print("\n SISTEM CALL CENTER ")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Pelanggan Terdepan")
        print("4. Tampilkan Antrean")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilihan == 1:
            nama = input("Masukkan nama pelanggan: ")
            call_center.enqueue(nama)

        elif pilihan == 2:
            call_center.dequeue()

        elif pilihan == 3:
            call_center.peek()

        elif pilihan == 4:
            call_center.display()

        elif pilihan == 5:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()