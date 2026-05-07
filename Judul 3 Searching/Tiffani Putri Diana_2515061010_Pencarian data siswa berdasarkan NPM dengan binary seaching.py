def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1

    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nilai: {arr[m]}")

        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari di kanan")
            l = m + 1
        else:
            print("Mencari di kiri")
            r = m - 1

    return pos


def main():
    arr = [2515061101, 2515061104, 2515061107, 2515061110, 2515061115, 2515061120]
    n = len(arr)

    print("Data NPM siswa:", arr)

    while True:
        try:
            target = int(input("Masukkan NPM yang dicari: "))
            break
        except ValueError:
            print("Input tidak valid!")

    pos = binary_search(arr, n, target)

    if pos != -1:
        print(f"Data ditemukan pada indeks ke-{pos}")
    else:
        print("Data tidak ditemukan")


if __name__ == "__main__":
    main()   