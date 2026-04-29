def format_rupiah(angka):
    hasil = f"{angka:,}".replace(",", ".")
    return f"Rp {hasil},-"

def menu():
    print("\n=== DAFTAR HARGA BARANG ===")
    print("1. Masukkan harga barang")
    print("2. Tampilkan semua harga barang")
    print("3. Keluar")
 
def main():
    nama_barang = ["Beras", "Gula", "Minyak", "Tepung", "Garam"]
    harga = [0] * 5

    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print("Masukkan harga 5 barang:")
            for i in range(5):
                while True:
                    try:
                        harga[i] = int(input(f"  Harga {nama_barang[i]}: Rp "))
                        break
                    except ValueError:
                        print("  Input tidak valid, masukkan angka!")
            print("Data harga berhasil disimpan!")

        elif choice == 2:
            print("\nNo  Nama Barang    Harga")
            for i in range(5):
                print(f"{i+1}.  {nama_barang[i]:<12}  {format_rupiah(harga[i])}")

        elif choice == 3:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()