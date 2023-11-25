# import pandas as pd
# import os
# # from login_user import current_username

# def clear():
#     os.system('cls')

# def rekap_penjualan():
#     clear()
#     # Membaca data transaksi dari file CSV
#     df = pd.read_csv('data_transaksi.csv')

#     # Mengonversi kolom 'Tanggal Transaksi' ke tipe datetime dan format ulang tanggal
#     df['Tanggal Transaksi'] = pd.to_datetime(df['Tanggal Transaksi'], format='%d-%m-%Y').dt.strftime('%d-%m-%Y')

#     # Menambahkan kolom No sebagai nomor urut
#     df['No'] = range(1, len(df) + 1)

#     rekap_penjualan = df.groupby(['Tanggal Transaksi', 'Username'], as_index=False).first().sort_values(by=['Tanggal Transaksi', 'Username', 'No'])

#     rekap_penjualan['Jumlah Pembelian'] = df.groupby(['Tanggal Transaksi', 'Username'])['Jumlah Pembelian'].sum().values
#     rekap_penjualan['Total Harga'] = df.groupby(['Tanggal Transaksi', 'Username'])['Total Harga'].sum().values

#     print("="*76)
#     print("| No | Tanggal Transaksi | Username | Nama Produk | Jumlah Pembelian | Total Harga |")
#     print("|" + "-"*74 + "|")
#     for index, row in rekap_penjualan.iterrows():
#         print(f"| {row['No']:>2} | {row['Tanggal Transaksi']:>16} | {row['Username']:>8} | {row['Nama Produk']:>12} | {row['Jumlah Pembelian']:>16} | {row['Total Harga']:>11} |")
#     print("="*76)
#     input("Klik ENTER untuk kembali!")
#     # main_menu()
    
    
# def deret_bilangan_genap(n):
#   deret = []
#   for i in range(2, n + 1, 2):
#     deret.append(i)
#   return deret

# def main():
#   # Menampilkan deret bilangan genap dari 2 hingga 10
#   deret = deret_bilangan_genap(10)
#   print(deret)

# main()


# # Menggunakan fungsi untuk mencetak beberapa nilai deret eksponensial
# for i in range(0, 5):
#     print(f'a{i} = {deret_eksponensial(i)}')
import os
import csv

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_positive_integer(value):
    return value.isdigit() and int(value) >= 0

def entri_stok():
    clear()

    # Cek jika file belum ada akan dibuat secara otomatis
    file_path = "data_pestisida.csv"
    if not os.path.exists(file_path):
        with open(file_path, mode="a", newline="") as data_pestisida:
            header = ['Nama', 'Stok', 'Ukuran', 'Harga (Rp)', 'Terjual']
            writer = csv.DictWriter(data_pestisida, fieldnames=header)
            writer.writeheader()

    # Membaca nama pestisida yang sudah ada
    list_pestisida = set()
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        list_pestisida.update(row['Nama'].title() for row in reader)

    # Membuka file CSV untuk menambahkan data
    with open(file_path, mode="a", newline="") as data_pestisida:
        header = ['Nama', 'Stok', 'Ukuran', 'Harga (Rp)', 'Terjual']
        writer = csv.DictWriter(data_pestisida, fieldnames=header)

        print("=" * 60)
        print("ENTRI STOK PESTISIDA".center(60))
        print("-" * 60)

        counter = True
        while counter:
            nama = input("Masukkan nama pestisida: ").strip().title()

            # Memeriksa apakah nama pestisida sudah ada atau kosong
            if not nama:
                print("Inputan tidak boleh kosong. Masukkan data kembali!")
                continue
            if nama in list_pestisida:
                print(f"Data pestisida {nama} sudah ada. Masukkan data lain!")
                continue

            stok = input("Masukkan stok pestisida: ")
            if not is_positive_integer(stok):
                print("Stok harus berupa angka non-negatif. Tambahkan data lain.")
                continue
            stok = int(stok)

            ukuran = input("Masukkan ukuran: ")
            if not ukuran:
                print("Ukuran tidak boleh kosong. Tambahkan data lain.")
                continue

            harga = input("Masukkan Harga (Rp): ")
            if not is_positive_integer(harga):
                print("Harga harus berupa angka non-negatif. Tambahkan data lain.")
                continue
            harga = int(harga)

            print("=" * 60)

            # Menulis data baru ke file CSV
            writer.writerow({'Nama': nama, 'Stok': stok, 'Ukuran': ukuran, 'Harga (Rp)': harga, 'Terjual': 0})
            print("Data berhasil disimpan!")
            print("-" * 60)

            while True:
                option = input("Tambah stok pestisida lagi? [y/n] : ").lower()
                if option == "y" or option == "n":
                    break
                else:
                    print("Masukkan pilihan yang benar!")

            if option == "n":
                counter = False
                print("-" * 60)
                print("Data berhasil disimpan!")

    # Menampilkan stok setelah entri
    tampilkan_stok()
    input("Klik ENTER untuk kembali!")
    pestisida()

def tampilkan_stok():
    # Fungsi untuk menampilkan stok pestisida
    with open("data_pestisida.csv", mode="r") as file:
        reader = csv.DictReader(file)
        print("=" * 60)
        print("STOK PESTISIDA".center(60))
        print("-" * 60)
        print(f"| {'Nama':<20} | {'Stok':<10} | {'Ukuran':<10} | {'Harga (Rp)':<15} | {'Terjual':<10} |")
        print("-" * 60)
        for row in reader:
            print(f"| {row['Nama']:<20} | {row['Stok']:<10} | {row['Ukuran']:<10} | {row['Harga (Rp)']:<15} | {row['Terjual']:<10} |")
        print("-" * 60)

# Fungsi ini hanya sebagai contoh. Sesuaikan dengan kebutuhan Anda.
def pestisida():
    print("Menu Pestisida")
    # ... (tambahkan pilihan menu Pestisida sesuai kebutuhan Anda)

# Pemanggilan fungsi entri_stok()
entri_stok()
