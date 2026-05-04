def bubble_sort_descending(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]

def main():
    print("\n   PERANGKINGAN SKOR PESERTA\n"  )

    try:
        n = int(input("Masukkan jumlah peserta: "))
        if n <= 0: return print("Jumlah peserta tidak valid!")
    except ValueError: return print("Input harus angka!")

    peserta = []
    for i in range(n):
        print(f"\nPeserta ke-{i+1}")
        nama = input("Nama  : ")
        try:
            skor = int(input("Skor  : "))
            if 0 <= skor <= 100:
                peserta.append([nama, skor])
            else:
                print("Skor harus 0-100! Data peserta ini dilewati."); continue
        except ValueError:
            print("Input salah! Data peserta ini dilewati."); continue

    print(f"\nData asli: {[p[1] for p in peserta]}")
    
    bubble_sort_descending(peserta)

    print(f"\n{'No':<5} {'Nama':<20} {'Skor':>6}\n" )
    for i, (nama, skor) in enumerate(peserta, 1):
        print(f"{i:<5} {nama:<20} {skor:>6}")


if __name__ == "__main__":
    main()