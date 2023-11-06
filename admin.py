import os
import csv
import login_admin
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
# -----------------------------------------Fungsi untuk MAIN MENU ADMIN---------------------------------------------------------------- 
def main_menu():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}  
    |{"Halaman Admin".center(58)}|
    |{"-"*58}|
    |{"[1]. Dashboard Tanaman".ljust(58)}|
    |{"[2]. Dashboard Pestisida".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Pilih Opsi: ")
    if option == "1":
        tanaman()
    elif option == "2":
        pestisida()
    else:
        input("Pilihan INVALID. Masukkan dengan benar! Klik ENTER untuk kembali!")
        main_menu()
     
# -----------------------------------------Fungsi untuk PAGE "TANAMAN"----------------------------------------------------------------
def entri_info():
    clear()

    # Mengecek file csv, jika belum ada akan dibuat secara otomatis
    if not os.path.isfile("info_tanaman.csv"):
        with open("info_tanaman.csv", 'w', newline="") as info_tanaman:
            header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
            writer = csv.DictWriter(info_tanaman, fieldnames=header)
            writer.writeheader()

    # Open the file in append mode outside the first if block
    with open("info_tanaman.csv", "a", newline="") as info_tanaman:
        header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
        writer = csv.DictWriter(info_tanaman, fieldnames=header)

        print("=" * 60)
        print("ENTRI INFO TANAMAN".center(60))
        print("-" * 60)

        counter = True
        while counter:
            nama = input("Masukkan nama tanaman: ")
            list_hama = []
            list_pestisida = []
            list_dosis = []

            while True:
                hama = input(f"Masukkan hama {nama} : ")

                pestisida = input(f"Masukkan pestisida untuk {hama} : ")
                dosis = input(f"Masukkan dosis untuk {pestisida} : ")

                list_hama.append(hama)
                list_pestisida.append(pestisida)
                list_dosis.append(dosis)

                print("-" * 60)
                option = input("Tambah hama, pestisida, dan dosis lagi? [y/n] : ")

                if option.lower() != "y":
                    break

            data = {'Nama': nama, 'Hama': list_hama, 'Pestisida': list_pestisida, 'Dosis': list_dosis}
            writer.writerow(data)
            info_tanaman.flush()

            print("-" * 60)
            option = input("Tambah data tanaman lagi? [y/n] : ")

            if option.lower() == "y":
                counter = True
            else:
                counter = False

    # Process the collected data
    hama_list = []
    pestisida_list = []
    dosis_list = []

    with open("info_tanaman.csv", "r", newline="") as info_tanaman:
        reader = csv.DictReader(info_tanaman)
        for row in reader:
            hama_list.extend(row['Hama'].split(', '))
            pestisida_list.extend(row['Pestisida'].split(', '))
            dosis_list.extend(row['Dosis'].split(', '))

    # Now, hama_list, pestisida_list, and dosis_list contain all the entries from the CSV file

    input("Data berhasil ditambahkan ke dalam file CSV. Klik ENTER untuk kembali")
    tanaman()

def tampilkan_info():
    clear()

    # Membaca data dari file CSV, dimulai dari baris ke-2
    with open("info_tanaman.csv", mode="r") as file:
        reader = csv.reader(file)
        rows = [row for row in reader]

    # Memisahkan nilai-nilai dalam list dan membentuk dataframe baru
    data = []
    for row in rows[1:]:
        nama = row[0]
        hama_list = [item.strip(" '[]") for item in row[1].split(',')]
        pestisida_list = [item.strip(" '[]") for item in row[2].split(',')]
        dosis_list = [item.strip(" '[]") for item in row[3].split(',')]

        for hama, pestisida, dosis in zip(hama_list, pestisida_list, dosis_list):
            data.append([nama, hama, pestisida, dosis])

    df = pd.DataFrame(data, columns=['Nama', 'Hama', 'Pestisida', 'Dosis'])
    df.index = range(1, len(df) + 1)  # Memulai index dari 1

    # Menampilkan dataframe
    print("=" * 60)
    print("DATA INFO TANAMAN".center(60))
    print("-" * 60)
    print(df)
    print("=" * 60)
    input("Klik ENTER untuk kembali!")
    tanaman()
    
def update_info():
    clear()
    # function untuk update data info tanaman

def hapus_info():
    clear()
    # function untuk hapus data info tanaman
 
# -----------------------------------------Fungsi untuk PAGE "PESTISIDA"----------------------------------------------------------------
def entri_stok():
    clear()
    # Cek jika file belum ada akan dibuat secara otomatis
    if not os.path.isfile("data_pestisida.csv"):
        with open("data_pestisida.csv", "w") as data_pestisida:
            header = ['Nama', 'Jumlah', 'Ukuran', 'Harga']
            writer= csv.DictWriter(data_pestisida, fieldnames=header)
            writer.writeheader()
    
    list_pestisida =[]
    with open("data_pestisida.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_pestisida.append(row)

    # Membuka file CSV untuk menambahkan data
    with open("data_pestisida.csv", mode="a", newline="") as data_pestisida:
        header = ['Nama', 'Jumlah', 'Ukuran', 'Harga']
        writer = csv.DictWriter(data_pestisida, fieldnames=header)
        
        # Menulis header jika file kosong
        if data_pestisida.tell() == 0:
            writer.writeheader()
        
        print("="*60)
        print("ENTRI STOK PESTISIDA".center(60))
        print("-"*60)
        
        nama = input("Masukkan nama pestisida: ")

        # Memeriksa apakah pestisida sudah ada di dalam list
        for data in list_pestisida:
            if nama == data['Nama']:
                print(f"Data pestisida {nama} sudah ada. Tambahkan data lain.")
                input("Klik ENTER untuk kembali!")
                entri_stok()

        jumlah = int(input("Masukkan jumlah stok pestisida: "))
        ukuran = input("Masukkan ukuran: ")
        harga = int(input("Masukkan harga (Rp): "))
        print("="*60)
        
        # Menulis data baru ke file CSV
        writer.writerow({'Nama': nama, 'Jumlah': jumlah, 'Ukuran': ukuran, 'Harga': harga})
        input("Data berhasil disimpan!. Klik ENTER untuk kembali!")
    
    pestisida()
    
def tampilkan_stok():
    clear()
    df = pd.read_csv("data_pestisida.csv")
    df.index = range(1, len(df) + 1)
    print("="*58)
    print("DATA STOK PESTISIDA".center(58))
    print("-"*58)
    print(df)
    print("="*58)
    input("Klik ENTER untuk kembali ke dashboard!")
    pestisida()
    
def update_stok():
    clear()
    list_pestisida = []
    with open("data_pestisida.csv", mode="r") as file: #buat buka file csv nya
        reader = csv.DictReader(file)
        for row in reader:
            list_pestisida.append(row) #membaca file csv tiap barisnya 
    
    nama = input("Masukkan nama pestisida yang ingin diupdate: ") #menginputkan nama pestisida yg mau diubah
    found = False 
    
    for data in list_pestisida:
        if nama == data['Nama']:
            found = True

            jumlah = int(input("Masukkan jumlah stok pestisida baru: "))
            ukuran = int(input("Masukkan ukuran baru: "))
            harga = int(input("Masukkan harga (Rp) baru: "))
            
            data['Jumlah'] = str(jumlah)
            data['Ukuran'] = str(ukuran)
            data['Harga'] = str(harga)
            
            with open("data_pestisida.csv", mode="w", newline="") as data_pestisida:
                header = ['Nama', 'Jumlah', 'Ukuran', 'Harga']
                writer = csv.DictWriter(data_pestisida, fieldnames=header)
                writer.writeheader()
                writer.writerows(list_pestisida)
            print(f"Data pestisida {nama} berhasil diupdate!")
            break
    
    if not found:
        print(f"Pestisida dengan nama {nama} tidak ditemukan.")
    
    input("Klik ENTER untuk kembali!")
    pestisida()

def hapus_stok():
    clear()
    list_stok = []
    df = pd.read_csv("data_pestisida.csv")
    df.index = range(1, len(df) + 1)
    print("="*58)
    print("DATA STOK PESTISIDA".center(58))
    print("-"*58)
    print(df)
    print("="*58)
    # Baca data pestisida dari file CSV
    with open("data_pestisida.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_stok.append(row)

    nama = input("Masukkan nama pestisida yang ingin dihapus: ")
    found = False

    # Cari pestisida berdasarkan nama
    for data in list_stok:
        if nama == data['Nama']:
            found = True
            list_stok.remove(data)  # Hapus data pestisida dari list

            with open("data_pestisida.csv", mode="w", newline="") as data_pestisida:
                header = ['Nama', 'Jumlah', 'Ukuran', 'Harga']
                writer = csv.DictWriter(data_pestisida, fieldnames=header)
                writer.writeheader()
                writer.writerows(list_stok)  # Tulis kembali data tanpa pestisida yang dihapus

            print(f"Data pestisida {nama} berhasil dihapus!")
            break

    if not found:
        print(f"Pestisida dengan nama {nama} tidak ditemukan.")

    input("Klik ENTER untuk kembali ke menu Pestisida!")
    pestisida()

def tanaman():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}
    |{"Dashboard Tanaman".center(58)}|
    |{"-"*58}|
    |{"[1]. Entri Informasi Tanaman".ljust(58)}|
    |{"[2]. Tampilkan Informasi Tanaman".ljust(58)}|
    |{"[3]. Update Informasi Tanaman".ljust(58)}|
    |{"[4]. Hapus Informasi Tanaman".ljust(58)}|
    |{"[5]. Back".ljust(58)}|
    |{"[6]. Exit".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Pilih Opsi: ")
    if option == "1":
        entri_info()
    elif option == "2":
        tampilkan_info()
    elif option == "3":
        update_info()
    elif option == "4":
        hapus_info()
    elif option == "5":
        main_menu()
    elif option == "6":
        exit()
    else:
        print("Pilihan INVALID. Masukkan pilihan yang sesuai!")
        input("Klik ENTER untuk kembali!")
        tanaman()
    
def pestisida():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}
    |{"Dashboard Pestisida".center(58)}|
    |{"-"*58}|
    |{"[1]. Entri Stok Pestisida".ljust(58)}|
    |{"[2]. Tampilkan Stok Pestisida".ljust(58)}|
    |{"[3]. Update Stok Pestisida".ljust(58)}|
    |{"[4]. Hapus Stok Pestisida".ljust(58)}|
    |{"[5]. Back".ljust(58)}|
    |{"[6]. Exit".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Pilih Opsi: ")
    if option == "1":
        entri_stok()
    elif option == "2":
        tampilkan_stok()
    elif option == "3":
        update_stok()
    elif option == "4":
        hapus_stok()
    elif option == "5":
        main_menu()
    elif option == "6":
        exit()
    else:
        print("Pilihan INVALID. Masukkan pilihan yang sesuai!")
        input("Klik ENTER untuk kembali!")
main_menu()