
def tukar(arr1, arr2, i, j):
    arr1[i], arr1[j] = arr1[j], arr1[i]
    arr2[i], arr2[j] = arr2[j], arr2[i]

def bubble_sort_descending(nama, skor, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if skor[j] < skor[j + 1]:
                tukar(nama, skor, j, j + 1)

def main():
    print("   PERANGKINGAN SKOR PESERTA")
    print("   Metode: Bubble Sort Descending")

    while True:
        try:
            n = int(input("\nMasukkan jumlah peserta: "))
            if n <= 0:
                print("Jumlah peserta harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Input tidak valid, masukkan angka!")

    nama = []
    skor = []

    print("\nMasukkan data peserta:")
    for i in range(n):
        print(f"\nPeserta ke-{i+1}")
        nama.append(input("Nama  : "))
        while True:
            try:
                nilai = int(input("Skor  : "))
                if nilai < 0 or nilai > 100:
                    print("Skor harus antara 0 - 100!")
                    continue
                skor.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, masukkan angka!")

    print(f"\nData sebelum diurutkan: {skor}")

    bubble_sort_descending(nama, skor, n)

    print("\nData setelah diurutkan (Bubble Sort Descending):")
    print(f"{'No':<5} {'Nama':<20} {'Skor':>6}")
    for i in range(n):
        print(f"{i+1:<5} {nama[i]:<20} {skor[i]:>6}")
    print("-" * 40)

if __name__ == "__main__":
    main()