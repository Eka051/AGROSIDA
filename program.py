import os
import csv
import pandas as pd
import login

def clear():
    os.system('cls')

def back():
    back = input("Klik \"ENTER\" Untuk Kembali")
    main_menu()
    print(back)
    
def main_menu():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}
    |{"[1]. Informasi Tanaman dan Pestisida".ljust(58)}|
    |{"[2]. Tambah Stok Pestisida".ljust(58)}|
    |{"[3]. Hapus Data Pestisida".ljust(58)}|
    |{"[4]. Tambah Transaksi".ljust(58)}|
    |{"[5]. Informasi Penjualan".ljust(58)}|
    {'='*60}
    ''')
    option = int(input("Masukkan Nomor Untuk Memilih Opsi: "))
    if option == 1:
        info_1 = open("info_tanaman.txt")
        info_2 = info_1.readlines()[0:40]
        for a in info_2:
            print(a)
    # elif option == 2:
    #     add_stock():
    # elif option == 3:
    #     delete_stock()
    # elif option == 4:
    #     add_transaction()
    # elif option == 5:
    #     sales_info()
    # else:
    #     print("Masukkan Pilihan Yang Benar")
    #     back()
    
    
# def info():
#     clear()
#     list_tanaman = []
#     with open("info_tanaman.txt", mode="r") as info_tanaman:
#         reader = csv.DictReader(info_tanaman)
#         for row in reader:
#             list_tanaman.append(row)

main_menu()