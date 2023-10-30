import os
import csv
import pandas as pd
import login

def clear():
    os.system('cls')

# def back():
#     back = input("Klik \"ENTER\" Untuk Kembali")
#     main_menu()
#     print(back)
    
def main_menu():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}
    |{"[1]. Informasi Tanaman".ljust(58)}|
    |{"[2]. Pestisida".ljust(58)}|
    |{"[3]. Rekap Penjualan".ljust(58)}|
    {'='*60}
    ''')
    option = int(input("Masukkan Nomor Untuk Memilih Opsi: "))
    if option == 1:
        info_tanaman()
    elif option == 2:
        menu_pestisida()
    elif option == 3:
        rekap_penjualan()
    else:
        input("Masukkan Pilihan Yang Benar. Klik ENTER untuk kemabali")
        main_menu()
    
def info_tanaman():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}
    |{"[1]. Tampilkan Informasi Tanaman".ljust(58)}|
    |{"[2]. Entri Informasi Tanaman".ljust(58)}|
    |{"[3]. Edit Informasi Tanaman".ljust(58)}|
    |{"[4]. Update Informasi Tanaman".ljust(58)}|
    |{"[5]. Hapus Informasi Tanaman".ljust(58)}|
    {'='*60}
    ''')
    option = int(input("Masukkan Pilihan: "))
    
    if option == 1:
        show_data()
    elif option == 2:
        entri_data()
    elif option == 3:
        edit_data()
    elif option == 4:
        update_data()
    elif option == 5:
        delete_data()
    else:
        input("Masukkan Pilihan Yang Benar. Klik ENTER untuk kembali")
        info_tanaman()
    
def info_tanaman():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}
    |{"[1]. Tambah Transaksi Pestisida".ljust(58)}|
    |{"[2]. Tampilkan Transaksi".ljust(58)}|
    {'='*60}
    ''')
    option = int(input("Masukkan Pilihan: "))
    
def rekap_penjualan():
    clear()
    
    
    
    
    
main_menu()