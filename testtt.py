import pandas as pd
import os
import csv

def clear():
    os.system('cls')

# def tampilkan_stok():
#     clear()
#     df = pd.read_csv("data_pestisida.csv")
#     df['Terjual'] = df['Terjual'].astype('int')
#     df.index = range(1, len(df) + 1)

#     # Menentukan lebar kolom
#     col_widths = {
#         "No": 3,
#         "Nama": 28,
#         "Jumlah": 8,
#         "Ukuran": 5,
#         "Harga (Rp)": 10,
#         "Terjual": 10
#     }

#     # Menambah kolom 'Nomor'
#     df.insert(0, 'No', range(1, len(df) + 1))

#     # Menampilkan header
#     print("="*77)
#     print(f'|{"DATA STOK PESTISIDA".center(75)}|')
#     print("-"*77)
#     print("|" + "|".join(f"{col.center(col_widths[col] + 1)}" for col in df.columns) + "|")
#     print("|" + "|".join("-" * (col_widths[col] + 1) for col in df.columns) + "|")

#     # Menampilkan data
#     for _, row in df.iterrows():
#         row_str = f"|{str(row['No']).center(col_widths['No'] + 1)}"  # No kolom rata tengah
#         row_str += f"|{str(row['Nama']).ljust(col_widths['Nama'] + 1)}"  # Nama kolom rata kiri
#         for col in df.columns[2:]:  # Kolom selanjutnya rata tengah
#             row_str += f"|{str(row[col]).center(col_widths[col] + 1)}"
#         print(row_str + "|")

#     print("="*77)

# tampilkan_stok()
# def tampilkan_stok():
#     clear()
#     df = pd.read_csv("data_pestisida.csv")
#     df.index = range(1, len(df) + 1)
#     print("="*68)
#     print("PRODUK PESTISIDA".center(68))
#     print("-"*68)
#     print(df)
#     print("="*68)
    
# def entri_stok():
#     clear()
#     # Cek jika file belum ada akan dibuat secara otomatis
#     if not os.path.exists("data_pestisida.csv"):
#         with open("data_pestisida.csv", mode="a", newline="") as data_pestisida:
#             header = ['Nama', 'Stok', 'Ukuran', 'Harga (Rp)', 'Terjual']
#             writer = csv.DictWriter(data_pestisida, fieldnames=header)
#             writer.writeheader()
                    
#     list_pestisida = []
#     with open("data_pestisida.csv", mode="r") as file:
#         reader = csv.DictReader(file)
#         list_pestisida = [row['Nama'].title() for row in reader]  # Untuk mengenali data stok pestisida yang sama menggunakan title case

#     # Membuka file CSV untuk menambahkan data menggunakan mode 'append'
#     with open("data_pestisida.csv", mode="a", newline="") as data_pestisida:
#         header = ['Nama', 'Stok', 'Ukuran', 'Harga (Rp)', 'Terjual']
#         writer = csv.DictWriter(data_pestisida, fieldnames=header)
#         print("=" * 60)
#         print("ENTRI STOK PESTISIDA".center(60))
#         print("-" * 60)
        
#         while True:
#             # Membaca data pestisida dari dalam file csv untuk memeriksa nama pestisida yang sama
#             list_pestisida = []
#             with open("data_pestisida.csv", mode="r") as file:
#                 reader = csv.DictReader(file)
#                 list_pestisida = [row['Nama'].title() for row in reader] # Untuk mengenali data pestisida yang sama menggunakan title case
                
#             nama = input("Masukkan nama pestisida: ").strip().title()
#             # Memeriksa apakah nama pestisida sudah ada atau kosong
#             if not nama:
#                 print("Inputan tidak boleh kosong. Masukkan data kembali!\n")
#                 continue
#             if nama in list_pestisida:
#                 print(f"Data pestisida {nama} sudah ada. Masukkan data lain!\n")
#                 continue
#             if len(nama) <= 3:
#                 print("Nama pestisida harus lebih dari 3 karakter\n")
#                 continue
#             while True:    
#                 stok = input("Masukkan stok pestisida: ").strip()
#                 if not stok.isdigit():
#                     print("Stok harus berupa angka. Tambahkan data lain.\n")
#                     continue
#                 stok = int(stok)
#                 if stok > 0:
#                     break
#                 else:
#                     print("Stok tidak boleh 0. Masukkan data lagi!\n")
#             while True: 
#                 ukuran = input("Masukkan ukuran: ").strip()
#                 if not ukuran:
#                     print("Ukuran tidak boleh kosong. Tambahkan data lain.\n")
#                     continue
#                 break
                
#             while True:
#                 harga = input("Masukkan Harga (Rp): ").strip()
                
#                 if not harga.isdigit():
#                     print("Harga harus berupa angka. Masukkan harga dengan benar.\n")
#                     continue
#                 harga = int(harga)
#                 if harga <= 10000:
#                     print("Harga harus lebih dari 10000. Masukkan harga yang sesuai!\n")
#                 else:
#                     break

#             print("=" * 60)
            
#             # Menulis data baru ke file CSV
#             writer.writerow({'Nama': nama, 'Stok': stok, 'Ukuran': ukuran, 'Harga (Rp)': harga, 'Terjual': 0})
#             data_pestisida.flush() # Untuk langsung menyimpan inputan ke file csv
#             os.fsync(data_pestisida.fileno()) # Untuk memastikan bahwa data sudah tersimpan
#             print("Data berhasil disimpan!")
#             print("-" * 60)
            
#             while True:
#                 option = input("Tambah stok pestisida lagi? [y/n] : ").strip().lower()
#                 print("-"*60)
#                 if option == "y":
#                     break
#                 elif option == "n":
#                     tampilkan_stok()
#                     print("-" * 60)
#                     print("Data berhasil disimpan!")
#                     return
#                 elif not option:
#                     print("Inputan tidak boleh kosong!\n")
#                 else:
#                     print("Masukkan pilihan yang benar!")

# # Panggil fungsi entri_stok
# entri_stok()
def entri_info():
    clear()
    header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
    if not os.path.exists("info_tanaman.csv"):
        with open("info_tanaman.csv", mode="a", newline="") as info_tanaman:
            writer = csv.DictWriter(info_tanaman, fieldnames=header)
            writer.writeheader()

    list_tanaman = []
    with open("info_tanaman.csv", mode="r") as file:
        reader = csv.DictReader(file)
        list_tanaman.extend(row['Nama'] for row in reader)

    print("=" * 60)
    print("ENTRI INFO TANAMAN".center(60))
    print("-" * 60)

    while True:
        list_tanaman = []
        with open("info_tanaman.csv", mode="r") as file:
            reader = csv.DictReader(file)
            list_tanaman.extend(row['Nama'] for row in reader)
            
        nama = input("Masukkan nama tanaman: ").strip().title()
        if not nama or not nama.isalpha():
            print("Inputan nama tanaman tidak boleh kosong dan harus berupa huruf! Masukkan kembali!")
            continue
        if nama in list_tanaman:
            print(f"Data tanaman {nama} sudah ada! Masukkan data lain!")
            continue

        tanaman_data = {'Nama': nama, 'Hama': [], 'Pestisida': [], 'Dosis': []}

        while True:
            hama = input(f"Masukkan hama {nama} : ").strip()
            if not hama:
                print("Inputan tidak boleh kosong! Masukkan data kembali!")
                continue

            pestisida = input(f"Masukkan pestisida untuk {hama} : ").strip()
            if not pestisida:
                print("Inputan tidak boleh kosong! Masukkan data kembali!")
                continue

            dosis = input(f"Masukkan dosis untuk {pestisida} : ").strip()
            if not dosis:
                print("Inputan tidak boleh kosong! Masukkan data kembali!")
                continue

            tanaman_data['Hama'].append(hama)
            tanaman_data['Pestisida'].append(pestisida)
            tanaman_data['Dosis'].append(dosis)

            while True:
                option = input("Tambah hama, pestisida, dan dosis lagi? [y/n] : ").strip().lower()
                print("-" * 60)
                if option in ["y", "n"]:
                    break
                elif not option:
                    print("Inputan tidak boleh kosong!\n")
                else:
                    print("Masukkan pilihan yang benar! (y/n)\n")

            if option == "n":
                break

        with open("info_tanaman.csv", mode="a", newline="") as info_tanaman:
            writer = csv.DictWriter(info_tanaman, fieldnames=header)
            writer.writerow(tanaman_data)
            info_tanaman.flush()
            os.fsync(info_tanaman.fileno())

        print("-" * 60)
        while True:
            option = input("Tambah data tanaman lagi? [y/n] : ").strip().lower()
            if option in ["y", "n"]:
                break
            elif not option:
                print("Inputan tidak boleh kosong!\n")
            else:
                print("Masukkan pilihan yang benar! (y/n)\n")

        if option == "n":
            break

    print("-" * 60)
    hama_list = []
    pestisida_list = []
    dosis_list = []

    with open("info_tanaman.csv", mode="r") as info_tanaman:
        reader = csv.DictReader(info_tanaman)
        for row in reader:
            hama_list.extend(row['Hama'])
            pestisida_list.extend(row['Pestisida'])
            dosis_list.extend(row['Dosis'])

    input("Data berhasil ditambahkan. Klik ENTER untuk kembali")

entri_info()
