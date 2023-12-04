import pandas as pd
import os
import csv
# # from login_user import current_username

def clear():
    os.system('cls')

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
def entri_info():
    clear()

    # Mengecek file csv, jika belum ada akan dibuat secara otomatis
    header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
    if not os.path.exists("info_tanaman.csv"):
        with open("TANAMAN.csv", mode="a", newline="") as info_tanaman:
            writer = csv.DictWriter(info_tanaman, fieldnames=header)
            writer.writeheader()

    # Membaca data tanaman yang sudah ada
    list_tanaman = []
    with open("info_tanaman.csv", mode="r") as file:
        reader = csv.DictReader(file)
        list_tanaman.extend(row['Nama'] for row in reader) # Untuk mengenali data info tanaman yang sama menggunakan title case

    print("=" * 60)
    print("ENTRI INFO TANAMAN".center(60))
    print("-" * 60)

    counter = True
    while counter:
        nama = input("Masukkan nama tanaman: ").strip().title()
        if not nama or not nama.isalpha():
            print("Inputan nama tanaman tidak boleh kosong dan harus berupa huruf! Masukkan kembali!")
            continue
        if nama in list_tanaman:
            print(f"Data tanaman {nama} sudah ada! Masukkan data lain!")
            continue

        list_hama = []
        list_pestisida = []
        list_dosis = []

        while True:
            hama = input(f"Masukkan hama {nama} : ").strip()
            if not hama or hama == "0":
                print("Inputan tidak boleh kosong! Masukkan data kembali!")
                continue
            if not hama or not hama.isalpha():
                print("Inputan hama tanaman tidak boleh kosong dan harus berupa huruf! Masukkan kembali!")
                continue
            break
        while True:
            pestisida = input(f"Masukkan pestisida untuk {hama} : ").strip()
            if not pestisida or pestisida == "0":
                print("Inputan tidak boleh kosong! Masukkan data kembali!")
                continue
            if not pestisida == "~!@#$%^&*()_+=-`<:<>?,./;":
                print("Inputan tidak boleh simbol atau kosong harus huruf atau angka")
                continue
            break
        while True:
            dosis = input(f"Masukkan dosis untuk {pestisida} : ").strip()
            if not dosis or dosis == "0":
                print("Inputan tidak boleh kosong atau 0! Masukkan data kembali!")
                continue
            break

            # Menambahkan hasil inputan ke dalam list
        list_hama.append(hama)
        list_pestisida.append(pestisida)
        list_dosis.append(dosis)

        print("-" * 60)
        while True:
            option = input("Tambah hama, pestisida, dan dosis lagi? [y/n] : ").strip()

            if option.lower() == "y" or option.lower() == "n":
                break
            else:
                print("Masukkan pilihan yang benar!")

        if option.lower() == "n":
            break
entri_info()