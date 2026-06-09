# NODE
class Node:
    def __init__(self, key, value):
        self.key   = key   
        self.value = value  
        self.next  = None


# HASH MAP (Separate Chaining) 
class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE  = size
        self.table = [None] * self.SIZE

    # Fungsi hash: memetakan string key ke indeks tabel
    def hash_function(self, key):
        total = 0
        for karakter in key:
            total += ord(karakter)
        return total % self.SIZE

    # Tambah / update produk
    def insert(self, key, value):
        index   = self.hash_function(key)
        current = self.table[index]

        # Jika key sudah ada → update value-nya
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Key belum ada → sisipkan di depan chain
        new_node      = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    # Cari produk berdasarkan key
    def search(self, key):
        index   = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    # Hapus produk berdasarkan key
    def remove_key(self, key):
        index   = self.hash_function(key)
        current = self.table[index]
        prev    = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev    = current
            current = current.next
        return False

    # Tampilkan seluruh isi tabel hash (untuk debug/info)
    def display_table(self):
        print("\n  Isi Hash Table (Separate Chaining):")
        for i in range(self.SIZE):
            print(f"  [{i}] ", end="")
            current = self.table[i]
            if current is None:
                print("(kosong)")
            else:
                while current is not None:
                    print(f"({current.key}, {current.value['nama']}) -> ", end="")
                    current = current.next
                print("None")
        print()


# KERANJANG BELANJA
class KeranjangBelanja:
    def __init__(self):
        self.hashmap = HashMapSeparateChaining(size=10)

    # Tambah produk ke keranjang
    def tambah_produk(self, id_produk, nama, harga, jumlah=1):
        node = self.hashmap.search(id_produk)
        if node:
            # Produk sudah ada → tambah jumlahnya
            node.value['jumlah'] += jumlah
            print(f"  [UPDATE] '{nama}' jumlah menjadi "
                  f"{node.value['jumlah']} pcs.")
        else:
            # Produk baru → insert ke hash map
            value = {
                'nama'  : nama,
                'harga' : harga,
                'jumlah': jumlah
            }
            self.hashmap.insert(id_produk, value)
            print(f"  [TAMBAH] '{nama}' berhasil ditambahkan "
                  f"(Rp {harga:,.0f} x {jumlah} pcs).")

    # Kurangi jumlah produk (hapus jika jumlah jadi 0)
    def kurangi_produk(self, id_produk, jumlah=1):
        node = self.hashmap.search(id_produk)
        if node is None:
            print(f"  [ERROR] Produk '{id_produk}' tidak ada di keranjang.")
            return
        nama = node.value['nama']
        if node.value['jumlah'] <= jumlah:
            self.hashmap.remove_key(id_produk)
            print(f"  [HAPUS] '{nama}' dihapus dari keranjang.")
        else:
            node.value['jumlah'] -= jumlah
            print(f"  [UPDATE] '{nama}' jumlah menjadi "
                  f"{node.value['jumlah']} pcs.")

    # Hapus produk sepenuhnya dari keranjang
    def hapus_produk(self, id_produk):
        node = self.hashmap.search(id_produk)
        if node is None:
            print(f"  [ERROR] Produk '{id_produk}' tidak ditemukan.")
            return
        nama = node.value['nama']
        self.hashmap.remove_key(id_produk)
        print(f"  [HAPUS] '{nama}' berhasil dihapus dari keranjang.")

    # Cari produk di keranjang
    def cari_produk(self, id_produk):
        node = self.hashmap.search(id_produk)
        if node:
            v = node.value
            print(f"\n  Produk ditemukan:")
            print(f"    ID     : {id_produk}")
            print(f"    Nama   : {v['nama']}")
            print(f"    Harga  : Rp {v['harga']:,.0f}")
            print(f"    Jumlah : {v['jumlah']} pcs")
            print(f"    Subtotal: Rp {v['harga'] * v['jumlah']:,.0f}")
        else:
            print(f"  [INFO] Produk '{id_produk}' tidak ada di keranjang.")

    # Tampilkan semua produk di keranjang (struk)
    def tampilkan_keranjang(self):  
        print("         KERANJANG BELANJA ANDA")
        print(f"  {'No':<4} {'ID':<6} {'Nama Produk':<18} {'Harga':>10} {'Qty':>4} {'Subtotal':>12}")
    

        ada_isi = False
        total   = 0
        nomor   = 1

        for i in range(self.hashmap.SIZE):
            current = self.hashmap.table[i]
            while current is not None:
                v        = current.value
                subtotal = v['harga'] * v['jumlah']
                total   += subtotal
                print(f"  {nomor:<4} {current.key:<6} {v['nama']:<18} "
                      f"Rp {v['harga']:>7,.0f} {v['jumlah']:>4} "
                      f"Rp {subtotal:>9,.0f}")
                nomor   += 1
                ada_isi  = True
                current  = current.next

        if not ada_isi:
            print("  (Keranjang kosong)")

       
        print(f"  {'TOTAL':>42} Rp {total:>9,.0f}")
        
    # Hitung total harga
    def total_harga(self):
        total = 0
        for i in range(self.hashmap.SIZE):
            current = self.hashmap.table[i]
            while current is not None:
                v      = current.value
                total += v['harga'] * v['jumlah']
                current = current.next
        return total

    # Checkout / kosongkan keranjang
    def checkout(self):
        if self.total_harga() == 0:
            print("  [INFO] Keranjang kosong, tidak ada yang di-checkout.")
            return
        self.tampilkan_keranjang()
        print(f"\n  Pembayaran sebesar Rp {self.total_harga():,.0f} berhasil.")
        print("  Terima kasih telah berbelanja!")
        # Kosongkan tabel
        self.hashmap.table = [None] * self.hashmap.SIZE


# ── MENU UTAMA ───────────────────────────────────────────────
def menu():
    print("       SISTEM KERANJANG BELANJA")
    print("  1. Tambah produk ke keranjang")
    print("  2. Kurangi jumlah produk")
    print("  3. Hapus produk dari keranjang")
    print("  4. Cari produk di keranjang")
    print("  5. Tampilkan keranjang")
    print("  6. Lihat struktur hash table")
    print("  7. Checkout & bayar")
    print("  8. Keluar")



def main():
    keranjang = KeranjangBelanja()

    # Data produk katalog (simulasi)
    katalog = {
        "P001": ("Sepatu Lari Nike",  350000),
        "P002": ("Kaos Polos Putih",  120000),
        "P003": ("Celana Jogger",     180000),
        "P004": ("Topi Baseball",      85000),
        "P005": ("Tas Ransel",        275000),
        "P006": ("Kaus Kaki 3 Pcs",    45000),
        "P007": ("Jaket Windbreaker", 420000),
        "P008": ("Sandal Casual",     130000),
    }
    

    pilih = 0
    while pilih != 8:
        menu()
        try:
            pilih = int(input("  Pilihan: "))
        except ValueError:
            print("  [ERROR] Masukkan angka yang valid!")
            continue

        #  1. Tambah produk 
        if pilih == 1:
            print("\n  Katalog Produk:")
            print(f"  {'ID':<6} {'Nama Produk':<22} {'Harga':>10}")
            for pid, (nama, harga) in katalog.items():
                print(f"  {pid:<6} {nama:<22} Rp {harga:>7,.0f}")
            print()

            id_input = input("  Masukkan ID produk: ").strip().upper()
            if id_input not in katalog:
                print("  [ERROR] ID produk tidak ada di katalog.")
                continue

            try:
                qty = int(input("  Jumlah: "))
                if qty <= 0:
                    print("  [ERROR] Jumlah harus lebih dari 0.")
                    continue
            except ValueError:
                print("  [ERROR] Masukkan angka yang valid!")
                continue

            nama, harga = katalog[id_input]
            keranjang.tambah_produk(id_input, nama, harga, qty)

        # 2. Kurangi jumlah 
        elif pilih == 2:
            id_input = input("\n  ID produk yang dikurangi: ").strip().upper()
            try:
                qty = int(input("  Kurangi berapa? "))
                if qty <= 0:
                    print("  [ERROR] Jumlah harus lebih dari 0.")
                    continue
            except ValueError:
                print("  [ERROR] Masukkan angka yang valid!")
                continue
            keranjang.kurangi_produk(id_input, qty)

        # 3. Hapus produk 
        elif pilih == 3:
            id_input = input("\n  ID produk yang dihapus: ").strip().upper()
            keranjang.hapus_produk(id_input)

        #  4. Cari produk 
        elif pilih == 4:
            id_input = input("\n  ID produk yang dicari: ").strip().upper()
            keranjang.cari_produk(id_input)

        # 5. Tampilkan keranjang 
        elif pilih == 5:
            keranjang.tampilkan_keranjang()

        #  6. Lihat struktur hash table 
        elif pilih == 6:
            keranjang.hashmap.display_table()

        # 7. Checkout
        elif pilih == 7:
            keranjang.checkout()

        # 8. Keluar 
        elif pilih == 8:
            print("\n  Program selesai. Sampai jumpa!")

        else:
            print("  [ERROR] Pilihan tidak valid!")


if __name__ == "__main__":
    main()