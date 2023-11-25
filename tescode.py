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
def register():
    clear()
    heading()
    print("REGISTER".center(60))
    print("-" * 60)

    data_account = []
    # Membaca data user dari file csv
    with open("data_user.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_account.append(row)

    while True:
        username = input("Masukkan Username: ")
        if username.strip() and username != "0" and len(username) >= 3:
            # Mengecek jika inputan user sama dengan username yang telah terdaftar
            user_ready = False
            for account in data_account:
                if username == account['username']:
                    input("Username telah terdaftar. Masukkan username lain!")
                    user_ready = True
                    break

            if not user_ready:
                break
        else:
            print("Username tidak boleh kosong, 0, dan panjang harus lebih dari atau sama dengan 3!")

    while True:
        password = input("Masukkan Password: ")
        if password.strip() and password != "0" and len(password) >= 3:
            break
        else:
            print("Password tidak boleh kosong, 0, dan panjang harus lebih dari atau sama dengan 3!")

    print("=" * 60)
    # Lanjutan kode untuk menyimpan data ke file atau tindakan selanjutnya
