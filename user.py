import os
import csv
import login_user
import pandas as pd

def clear():
    os.system('cls')
    
def exit():
    clear()
    print(f'''
    {"="*60}
    |{"Terima Kasih Telah Menggunakan Program Kami :)".center(58)}|
    {"="*60}
    ''')
    
def info_tanaman():
    clear()
     # Membaca data dari file CSV, dimulai dari baris ke-2
    with open("info_tanaman.csv", mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = [row for row in reader]

    # Memisahkan nilai-nilai dalam list dan membentuk dataframe baru
    data = []
    for row in rows:
        nama = row[0]
        hama_list = [item.strip(" '[]") for item in row[1].split(',')]
        pestisida_list = [item.strip(" '[]") for item in row[2].split(',')]
        dosis_list = [item.strip(" '[]") for item in row[3].split(',')]

        for hama, pestisida, dosis in zip(hama_list, pestisida_list, dosis_list):
            data.append([nama, hama, pestisida, dosis])

    df = pd.DataFrame(data, columns=header)
    df.index = range(1, len(df) + 1) # Memulai index dari 1

    # Menampilkan dataframe
    print("="*60)
    print("DATA INFO TANAMAN".center(60))
    print("-"*60)
    print(df)
    print("="*60)
    input("Klik ENTER untuk kembali ke menu utama!")
    main_menu()
    
def beli_pestisida():
    clear()
    df = pd.read_csv("data_pestisida.csv")
    df.index = range(1, len(df) + 1)
    print("="*58)
    print("PRODUK PESTISIDA".center(58))
    print("-"*58)
    print(df)
    print("="*58)
    
    # Function untuk transaksi pestisida

def main_menu():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}  
    |{"HOME".center(58)}|
    |{"-"*58}|
    |{"[1]. Informasi Tanaman".ljust(58)}|
    |{"[2]. Beli Pestisida".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Pilih Opsi: ")
    if option == "1":
        info_tanaman()
    elif option == "2":
        beli_pestisida()
    else:
        input("Pilihan INVALID. Pilih Opsi Yang Tersedia!")
        main_menu()
        
main_menu()