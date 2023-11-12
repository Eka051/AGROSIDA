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
    |{"[3]. Rekap Penjualan".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Pilih Opsi: ")
    if option == "1":
        tanaman()
    elif option == "2":
        pestisida()
    elif option == "3":
        clear()
        print("="*60)
        print("DATA REKAP PENJUALAN".center(60))
        print("-"*60)
        print(rekap_penjualan())
        print("="*60)
        input("Klik ENTER untuk kembali!")
        main_menu()
    else:
        input("Pilihan INVALID. Masukkan dengan benar! Klik ENTER untuk kembali!")
        main_menu()
        
def rekap_penjualan():
    if not os.path.exists("transaksi.csv"):
        print("="*60)
        print("\nData rekap penjualan tidak ada. Klik ENTER untuk kembali!\n")
        print("="*60)
        input()
        main_menu()
        
    data = pd.read_csv("transaksi.csv")
    data['Tanggal'] = data['Tanggal Transaksi']
    
    # Merekap penjualan perhari
    rekap_per_hari = data.groupby(['Tanggal']).agg({ #agregasi data frame untuk menghitung jumlah penjualan
        'Jumlah Pembelian': 'sum',
        'Total Harga': 'sum',
    }).reset_index()
    
    rekap_per_hari.index = range(1, len(rekap_per_hari) + 1)
    rekap_per_hari.to_csv('rekap_penjualan.csv')
    return rekap_per_hari
     
# -----------------------------------------Fungsi untuk PAGE "TANAMAN"----------------------------------------------------------------

# Fungsi untuk kembali ke dashboard tanaman
def back_tanaman():
    tanaman()
    
# Fungsi untuk entri informasi tanaman (Nama, Hama, Pestisida, Dosis)    
def entri_info():
    clear()

    # Mengecek file csv, jika belum ada akan dibuat secara otomatis
    with open("info_tanaman.csv", mode="a", newline="") as info_tanaman:
        header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
        writer = csv.DictWriter(info_tanaman, fieldnames=header)
        if info_tanaman.tell() == 0: # Jika header kosong, maka akan dibuatkan header otomatis
            writer.writeheader()
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

                # Menambahkan hasil inputan ke dalam list
                list_hama.append(hama)
                list_pestisida.append(pestisida)
                list_dosis.append(dosis)

                print("-" * 60)
                option = input("Tambah hama, pestisida, dan dosis lagi? [y/n] : ")

                if option.lower() != "y":
                    break

            data = {'Nama': nama, 'Hama': list_hama, 'Pestisida': list_pestisida, 'Dosis': list_dosis}
            writer.writerow(data)

            print("-" * 60)
            option = input("Tambah data tanaman lagi? [y/n] : ")

            if option.lower() == "y":
                counter = True
            else:
                counter = False

    hama_list = []
    pestisida_list = []
    dosis_list = []
    
    with open("info_tanaman.csv", mode="r") as info_tanaman:
        reader = csv.DictReader(info_tanaman)
        for row in reader:
            hama_list.extend(row['Hama'].split(', '))
            pestisida_list.extend(row['Pestisida'].split(', '))
            dosis_list.extend(row['Dosis'].split(', '))
    print("-"*60)
    input("Data berhasil ditambahkan. Klik ENTER untuk kembali")
    back_tanaman()
    
# Fungsi untuk menampilkan informasi tanaman dari file csv ke terminal
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
     
# Fungsi untuk mengupdate informasi tanaman yang tersimpan di dalam file csv       
def update_info():
    clear()
    tampilkan_info()

    list_tanaman = []
    with open("info_tanaman.csv", mode="r") as file:
        reader = csv.DictReader(file)
        list_tanaman = [row for row in reader]

    while True:
        nama = input("Masukkan nama tanaman untuk diupdate: ")
        found = False
        for data in list_tanaman:
            if data['Nama'] == nama:
                found = True
                break

        if not found:
            print(f"Tanaman dengan nama {nama} tidak ditemukan.")
            cancel = input("Ketik \'b\' untuk kembali ke dashboard! : ")
            if cancel.lower() == "b":
                info_tanaman()
        # Menambahkan data hama, pestisida, dan dosis baru
        list_hama = []
        list_pestisida = []
        list_dosis = []
        while True:
            hama = input(f"Masukkan hama {nama} : ")

            pestisida = input(f"Masukkan pestisida untuk {hama} : ")
            dosis = input(f"Masukkan dosis untuk {pestisida} : ")

            # Menambahkan hasil inputan ke dalam list
            list_hama.append(hama)
            list_pestisida.append(pestisida)
            list_dosis.append(dosis)

            print("-" * 60)
            option = input("Tambah hama, pestisida, dan dosis lagi? [y/n] : ")

            if option.lower() != "y":
                break

        # Mengganti data tanaman di file CSV
        data['Hama'] = list_hama
        data['Pestisida'] = list_pestisida
        data['Dosis'] = list_dosis

        with open("info_tanaman.csv", mode="w", newline="") as info_tanaman:
            header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
            writer = csv.DictWriter(info_tanaman, fieldnames=header)
            writer.writeheader()
            writer.writerows(list_tanaman)

        tampilkan_info()
        print("-" * 60)
        print(f"Info tanaman {nama} berhasil diupdate")

        input("Klik ENTER untuk kembali!")
        back_tanaman()

# Fungsi untuk menghapus informasi tanaman di dalam file csv
def hapus_info():
    clear()
    tampilkan_info()
    # Membaca data tanaman dari file csv
    list_tanaman = []
    with open("info_tanaman.csv", mode="r") as file:
        reader = csv.DictReader(file)
        list_tanaman = [row for row in reader]

    while True:
        nama = input("Masukkan nama tanaman untuk dihapus: ")
        found = False
        for data in list_tanaman:
            if data['Nama'] == nama:
                found = True
                break

        if not found:
            print(f"Tanaman dengan nama {nama} tidak ditemukan.")
            input("Klik ENTER untuk kembali ke dashboard!")
            back_tanaman()
        else:
            confirm = input(f"Apakah Anda yakin ingin menghapus info tanaman {nama}? [y/n]: ")
            if confirm.lower() == "y":
                list_tanaman.remove(data)

                # Menuliskan kembali data tanaman setelah menghapus data yang dipilih
                with open("info_tanaman.csv", mode="w", newline="") as info_tanaman:
                    header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
                    writer = csv.DictWriter(info_tanaman, fieldnames=header)
                    writer.writeheader()
                    writer.writerows(list_tanaman)

                tampilkan_info()
                print("-" * 60)
                print(f"Info tanaman {nama} berhasil dihapus")

                input("Klik ENTER untuk kembali!")
                back_tanaman()

            elif confirm.lower() == "n":
                back_tanaman()
            else:
                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")

 
# -----------------------------------------Fungsi untuk PAGE "PESTISIDA"----------------------------------------------------------------
# Fungsi untuk entri stok pestisida dan menyimpannya ke dalam file csv
def entri_stok():
    clear()
    # Cek jika file belum ada akan dibuat secara otomatis
    if not os.path.exists("data_pestisida.csv"):
        with open("data_pestisida.csv", mode="a", newline="") as data_pestisida:
            header = ['Nama', 'Jumlah', 'Ukuran', 'Harga (Rp)', 'Terjual']
            writer= csv.DictWriter(data_pestisida, fieldnames=header)
            writer.writeheader()
                    
    list_pestisida = []
    with open("data_pestisida.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_pestisida.append(row)

    # Membuka file CSV untuk menambahkan data
    with open("data_pestisida.csv", mode="a", newline="") as data_pestisida:
        header = ['Nama', 'Jumlah', 'Ukuran', 'Harga (Rp)', 'Terjual']
        writer = csv.DictWriter(data_pestisida, fieldnames=header)
        
        print("="*60)
        print("ENTRI STOK PESTISIDA".center(60))
        print("-"*60)
        
        counter = True
        while counter:
            nama = input("Masukkan nama pestisida: ")
            # Memeriksa apakah pestisida sudah ada di dalam list
            for data in list_pestisida:
                if nama == data['Nama']:
                    print(f"Data pestisida {nama} sudah ada. Tambahkan data lain.")
                    input("Klik ENTER untuk kembali!")
                    entri_stok()
                    
            jumlah = int(input("Masukkan jumlah stok pestisida: "))
            ukuran = input("Masukkan ukuran: ")
            Harga = int(input("Masukkan Harga (Rp): "))
            print("="*60)
            
            # Menulis data baru ke file CSV
            writer.writerow({'Nama': nama, 'Jumlah': jumlah, 'Ukuran': ukuran, 'Harga (Rp)': Harga, 'Terjual': 0})
            print("Data berhasil disimpan!")
            print("-" * 60)
            option = input("Tambah stok pestisida lagi? [y/n] : ")

            if option.lower() == "y":
                counter = True
            else:
                counter = False
                print("-"*60)
                print("Data berhasil disimpan!")
    
    tampilkan_stok()
    input("Klik ENTER untuk kembali!")
    pestisida()

# Fungsi untuk menampilkan stok pestisida dari file csv ke terminal 
def tampilkan_stok():
    clear()
    df = pd.read_csv("data_pestisida.csv")
    df['Terjual'] = df['Terjual'].astype('int')
    df.index = range(1, len(df) + 1)
    print("="*68)
    print("DATA STOK PESTISIDA".center(68))
    print("-"*68)
    print(df)
    print("="*68)
 
# Fungsi untuk mengupdate (mengubah) data pestisida
def update_stok():
    clear()
    tampilkan_stok()
    list_pestisida = []
    with open("data_pestisida.csv", mode="r") as file: #buat buka file csv nya
        reader = csv.DictReader(file)
        for row in reader:
            list_pestisida.append(row) #membaca file csv tiap barisnya 
    
    no_produk = input("Pilih nomor pestisida untuk diupdate: ")
    if no_produk.isdigit():
        no_produk = int(no_produk)
        if 1 <= no_produk <= len(list_pestisida):
            data = list_pestisida[no_produk - 1]
            
            jumlah = int(input("Masukkan jumlah stok pestisida baru: "))
            ukuran = str(input("Masukkan ukuran baru: "))
            Harga = int(input("Masukkan Harga baru (Rp): "))
            
            data['Jumlah'] = str(jumlah)
            data['Ukuran'] = str(ukuran)
            data['Harga (Rp)'] = str(Harga)
            
            with open("data_pestisida.csv", mode="w", newline="") as data_pestisida:
                header = ['Nama', 'Jumlah', 'Ukuran', 'Harga (Rp)', 'Terjual']
                writer = csv.DictWriter(data_pestisida, fieldnames=header)
                writer.writeheader()
                writer.writerows(list_pestisida)
            tampilkan_stok()
            print("Data pestisida berhasil diupdate!")
            print("-"*68)
        else:
            input("Pilih data yang tersedia!. Klik ENTER untuk kembali!")
            update_stok()
    else:
        input("Pilihan berupa angka!")
        update_stok()
        
    input("Klik ENTER untuk kembali!")
    pestisida()

# Fungsi untuk menghapus stok pestisida
def hapus_stok():
    clear()
    tampilkan_stok()
    # Baca data pestisida dari file CSV
    list_stok = []
    with open("data_pestisida.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_stok.append(row)
            
    counter = True
    while counter:
        no_produk = input("Pilih nomor pestisida untuk yang ingin dihapus: ")     
        if no_produk.isdigit():
            no_produk = int(no_produk)
            if 1 <= no_produk <= len(list_stok):
                list_stok.pop(no_produk - 1)
                with open("data_pestisida.csv", mode="w", newline="") as data_pestisida:
                    header = ['Nama', 'Jumlah', 'Ukuran', 'Harga (Rp)', 'Terjual']
                    writer = csv.DictWriter(data_pestisida, fieldnames=header)
                    writer.writeheader()
                    writer.writerows(list_stok)  # Tulis kembali data tanpa pestisida yang dihapus
                tampilkan_stok()
                print("-"*60)
                print("Data pestisida berhasil dihapus!\n")
                
                option = input("Hapus stok pestisida lagi? [y/n] : ")

                if option.lower() == "y":
                    counter = True
                else:
                    counter = False
                    print("-"*60)
            else:
                input("Pilih data yang tersedia!. Klik ENTER untuk kembali!")
                hapus_stok()
        else:
            input("Pilihan berupa angka!")
            hapus_stok()
            
    input("\nKlik ENTER untuk kembali ke menu Pestisida!")
    pestisida()

#------------------------------------------------- Fungsi untuk DASHBOARD ------------------------------------------------------------
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
        input("Klik ENTER untuk kembali!")
        tanaman()
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
        input("Klik ENTER untuk kembali ke dashboard!")
        pestisida()
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
        
main_menu()