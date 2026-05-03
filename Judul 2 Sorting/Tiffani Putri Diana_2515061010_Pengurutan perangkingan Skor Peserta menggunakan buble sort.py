def tukar(arr, i, j):
    temp   = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort_descending(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                tukar(arr, j, j + 1)

def main():
    n = int(input("Masukkan jumlah peserta: "))

    nama = []
    skor = []

    print("Masukkan data peserta:")
    for i in range(n):
        print(f"\nPeserta ke-{i+1}")
        nama.append(input("Nama  : "))
        skor.append(int(input("Skor  : ")))

    print(f"\nData sebelum diurutkan: {skor}")

    bubble_sort_descending(skor, n)
    print("Data setelah diurutkan (Bubble Sort Descending):")
    print(f"\n{'No':<5} {'Nama':<20} {'Skor':>6}")
    for i in range(n):
            print(f"{i+1:<5} {nama[i]:<20} {skor[i]:>6}")
   
if __name__ == "__main__":
    main()
