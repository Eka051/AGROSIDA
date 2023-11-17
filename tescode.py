import pandas as pd
import os
# from login_user import current_username

def clear():
    os.system('cls')

def rekap_penjualan():
    clear()
    # Membaca data transaksi dari file CSV
    df = pd.read_csv('data_transaksi.csv')

    # Mengonversi kolom 'Tanggal Transaksi' ke tipe datetime dan format ulang tanggal
    df['Tanggal Transaksi'] = pd.to_datetime(df['Tanggal Transaksi'], format='%d-%m-%Y').dt.strftime('%d-%m-%Y')

    # Menambahkan kolom No sebagai nomor urut
    df['No'] = range(1, len(df) + 1)

    rekap_penjualan = df.groupby(['Tanggal Transaksi', 'Username'], as_index=False).first().sort_values(by=['Tanggal Transaksi', 'Username', 'No'])

    rekap_penjualan['Jumlah Pembelian'] = df.groupby(['Tanggal Transaksi', 'Username'])['Jumlah Pembelian'].sum().values
    rekap_penjualan['Total Harga'] = df.groupby(['Tanggal Transaksi', 'Username'])['Total Harga'].sum().values

    print("="*76)
    print("| No | Tanggal Transaksi | Username | Nama Produk | Jumlah Pembelian | Total Harga |")
    print("|" + "-"*74 + "|")
    for index, row in rekap_penjualan.iterrows():
        print(f"| {row['No']:>2} | {row['Tanggal Transaksi']:>16} | {row['Username']:>8} | {row['Nama Produk']:>12} | {row['Jumlah Pembelian']:>16} | {row['Total Harga']:>11} |")
    print("="*76)
    input("Klik ENTER untuk kembali!")
    # main_menu()
