import os
import csv
import pandas as pd
import login_admin

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
    |{"[4]. Exit".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Pilih Opsi: ")
    if option == "1":
        tanaman()
    elif option == "2":
        pestisida()
    elif option == "3":
        rekap_penjualan()
    elif option == "4":
        exit()
    else:
        input("Pilihan INVALID. Masukkan dengan benar! Klik ENTER untuk kembali!")
        main_menu()
        
def rekap_penjualan():
    clear()
    # Membaca data transaksi dari file CSV
    df = pd.read_csv('data_transaksi.csv')

    # Mengelompokkan data berdasarkan 'Tanggal Transaksi', 'Username', dan 'Nama Produk'
    grup_df = df.groupby(['Tanggal Transaksi', 'Username', 'Nama Produk'], as_index=False)

    # Menghitung jumlah pembelian dan total harga
    grup_df = grup_df[['Jumlah Pembelian', 'Total Harga']].sum()

    # Menambahkan kolom No sebagai nomor
    grup_df['No'] = range(1, len(grup_df) + 1)

    print("="*90)
    print("DATA REKAP PENJUALAN PER HARI".center(90))
    print("-"*90)
    print(grup_df[['No', 'Tanggal Transaksi', 'Username', 'Nama Produk', 'Jumlah Pembelian', 'Total Harga']].to_string(index=False))
    print("="*90)
    input("Klik ENTER untuk kembali!")
    main_menu()
     
# -----------------------------------------Fungsi untuk PAGE "TANAMAN"----------------------------------------------------------------

# Fungsi untuk kembali ke dashboard tanaman
def back_tanaman():
    tanaman()
    
# Fungsi untuk entri informasi tanaman (Nama, Hama, Pestisida, Dosis)    
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

        data_tanaman = {'Nama': nama, 'Hama': [], 'Pestisida': [], 'Dosis': []}

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

            data_tanaman['Hama'].append(hama)
            data_tanaman['Pestisida'].append(pestisida)
            data_tanaman['Dosis'].append(dosis)

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
            writer.writerow(data_tanaman)
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
    print("-" * 60)
    input("Data berhasil ditambahkan. Klik ENTER untuk kembali")
    back_tanaman()
    
# Fungsi untuk menampilkan informasi tanaman dari file csv ke terminal
def tampilkan_info():
    clear()
    # Membaca data dari file CSV, dimulai dari baris ke-2
    with open("info_tanaman.csv", mode="r") as file:
        reader = csv.reader(file)
        rows = [row for row in reader] # "rows" berisi list dari setiap baris dalam file CSV.
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
        # Menampilkan daftar tanaman dengan nomor urutan
        print("Pilih nomor tanaman yang ingin diupdate!")
        print("-"*60)
        for i, data in enumerate(list_tanaman, start=1):
            print(f"{i}. {data['Nama']}")
        print("-"*60)
        pilihan = input("Masukkan nomor tanaman: ").strip()
        if not pilihan:
            input("Masukkan nomor untuk memilih nama tanaman!")
            print("-"*60)
            continue
        
        if pilihan.isdigit():
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(list_tanaman):
                selected_tanaman = list_tanaman[pilihan - 1]
                break
            else:
                print("Nomor tanaman tidak valid. Silakan coba lagi.")
                print("-"*60)
        else:
            print("Masukkan nomor yang valid.")
            
    if selected_tanaman:
        list_hama = []
        list_pestisida = []
        list_dosis = []
        
        while True:
            hama = input(f"Masukkan hama {selected_tanaman['Nama']} : ").strip()
            pestisida = input(f"Masukkan pestisida untuk {hama} : ").strip()
            dosis = input(f"Masukkan dosis untuk {pestisida} : ").strip()

            # Memeriksa apakah ada input, jika kosong maka data tidak akan berubah
            if not hama or not pestisida or not dosis:
                break

            # Menambahkan hasil inputan ke dalam list
            list_hama.append(hama)
            list_pestisida.append(pestisida)
            list_dosis.append(dosis)

            print("-" * 60)
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

        # Mengganti data tanaman di file CSV hanya jika ada input
        if list_hama or list_pestisida or list_dosis:
            selected_tanaman['Hama'] = list_hama
            selected_tanaman['Pestisida'] = list_pestisida
            selected_tanaman['Dosis'] = list_dosis

            with open("info_tanaman.csv", mode="w", newline="") as info_tanaman:
                header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
                writer = csv.DictWriter(info_tanaman, fieldnames=header)
                writer.writeheader()
                writer.writerows(list_tanaman)

            tampilkan_info()
            print("-" * 60)
            input(f"Info tanaman {selected_tanaman['Nama']} berhasil diupdate. Klik ENTER untuk kembali")
            back_tanaman()
        else:
            print("Tidak ada input baru. Data tidak berubah.")
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
        print("Pilih nomor tanaman yang ingin dihapus!")
        print("-"*60)
        for i, data in enumerate(list_tanaman, start=1):
            print(f"{i}. {data['Nama']}")
            
        nomor_tanaman = input("Masukkan nomor tanaman untuk dihapus: ")

        if nomor_tanaman.isdigit():
            nomor_tanaman = int(nomor_tanaman)

            if 1 <= nomor_tanaman <= len(list_tanaman):
                confirm = input(f"Apakah Anda yakin ingin menghapus info tanaman {data['Nama']}? [y/n]: ")

                if confirm.lower() == "y":
                    list_tanaman.pop(nomor_tanaman - 1)

                    # Menuliskan kembali data tanaman setelah menghapus data yang dipilih
                    with open("info_tanaman.csv", mode="w", newline="") as info_tanaman:
                        header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
                        writer = csv.DictWriter(info_tanaman, fieldnames=header)
                        writer.writeheader()
                        writer.writerows(list_tanaman)

                    tampilkan_info()
                    print("-" * 60)
                    print(f"Info tanaman {data['Nama']} berhasil dihapus")

                    input("Klik ENTER untuk kembali!")
                    back_tanaman()

                elif confirm.lower() == "n":
                    back_tanaman()
                else:
                    input("Pilihan tidak valid. Klik ENTER untuk memilih kembali!")
                    hapus_info()
            else:
                print("Nomor tanaman tidak valid. Silakan pilih nomor tanaman yang tersedia.")
        else:
            print("Nomor tanaman harus berupa angka.")

# -----------------------------------------Fungsi untuk PAGE "PESTISIDA"----------------------------------------------------------------
def entri_stok():
    clear()
    # Cek jika file belum ada akan dibuat secara otomatis
    if not os.path.exists("data_pestisida.csv"):
        with open("data_pestisida.csv", mode="a", newline="") as data_pestisida:
            header = ['Nama', 'Stok', 'Ukuran', 'Harga (Rp)', 'Terjual']
            writer = csv.DictWriter(data_pestisida, fieldnames=header)
            writer.writeheader()
                    
    list_pestisida = []
    with open("data_pestisida.csv", mode="r") as file:
        reader = csv.DictReader(file)
        list_pestisida = [row['Nama'].title() for row in reader]

    with open("data_pestisida.csv", mode="a", newline="") as data_pestisida:
        header = ['Nama', 'Stok', 'Ukuran', 'Harga (Rp)', 'Terjual']
        writer = csv.DictWriter(data_pestisida, fieldnames=header)
        print("=" * 60)
        print("ENTRI STOK PESTISIDA".center(60))
        print("-" * 60)
        
        while True:
            # Membaca data pestisida dari dalam file csv untuk memeriksa jika ada nama pestisida yang sama
            list_pestisida = []
            with open("data_pestisida.csv", mode="r") as file:
                reader = csv.DictReader(file)
                list_pestisida = [row['Nama'].title() for row in reader]
                
            nama = input("Masukkan nama pestisida: ").strip().title()
            if not nama:
                print("Inputan tidak boleh kosong. Masukkan data kembali!\n")
                continue
            if nama in list_pestisida:
                print(f"Data pestisida {nama} sudah ada. Masukkan data lain!\n")
                continue
            if len(nama) <= 3:
                print("Nama pestisida harus lebih dari 3 karakter\n")
                continue
            while True:    
                stok = input("Masukkan stok pestisida: ").strip()
                if not stok.isdigit():
                    print("Stok harus berupa angka. Tambahkan data lain.\n")
                    continue
                stok = int(stok)
                if stok > 0:
                    break
                else:
                    print("Stok tidak boleh 0. Masukkan data lagi!\n")
            while True: 
                ukuran = input("Masukkan ukuran: ").strip()
                if not ukuran:
                    print("Ukuran tidak boleh kosong. Tambahkan data lain.\n")
                    continue
                break
                
            while True:
                harga = input("Masukkan Harga (Rp): ").strip()
                if not harga.isdigit():
                    print("Harga harus berupa angka. Masukkan harga dengan benar.\n")
                    continue
                harga = int(harga)
                if harga <= 10000:
                    print("Harga harus lebih dari 10000. Masukkan harga yang sesuai!\n")
                else:
                    break

            print("=" * 60)
            
            # Menulis data baru ke file CSV
            writer.writerow({'Nama': nama, 'Stok': stok, 'Ukuran': ukuran, 'Harga (Rp)': harga, 'Terjual': 0})
            data_pestisida.flush() # Untuk langsung menyimpan inputan ke file csv
            os.fsync(data_pestisida.fileno()) # Untuk memastikan bahwa data sudah tersimpan
            print("Data berhasil disimpan!")
            print("-" * 60)
            
            while True:
                option = input("Tambah stok pestisida lagi? [y/n] : ").strip().lower()
                print("-"*60)
                if option == "y":
                    break
                elif option == "n":
                    tampilkan_stok()
                    input("Klik ENTER untuk kembali!")
                    pestisida()
                    return
                elif not option:
                    print("Inputan tidak boleh kosong!\n")
                else:
                    print("Masukkan pilihan yang benar!")
    

# Fungsi untuk menampilkan stok pestisida dari file csv ke terminal 
def tampilkan_stok():
    clear()
    df = pd.read_csv("data_pestisida.csv")
    df.index = range(1, len(df) + 1)
    print("="*68)
    print("PRODUK PESTISIDA".center(68))
    print("-"*68)
    print(df)
    print("="*68)
 
# Fungsi untuk mengupdate (mengubah) data pestisida
def update_stok():
    clear()
    tampilkan_stok()
    list_pestisida = []

    with open("data_pestisida.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_pestisida.append(row)

    no_produk = input("Pilih nomor pestisida untuk diupdate: ")

    if not no_produk.strip():
        print("Pilihan tidak valid. Silakan masukkan nomor pestisida yang ingin diupdate.")
        input("Klik ENTER untuk kembali!")
        pestisida()
        return

    if no_produk.isdigit():
        no_produk = int(no_produk)

        if 1 <= no_produk <= len(list_pestisida):
            data = list_pestisida[no_produk - 1]

            while True:
                stok = input("Masukkan stok pestisida baru: ")
                if stok.strip() and stok.isdigit() and stok != 0:
                    data['Stok'] = int(stok)
                    break
                else:
                    print("Stok berupa angka dan tidak boleh 0. Masukkan data kembali!")
            while True:
                ukuran = input("Masukkan ukuran baru: ")
                if ukuran.strip():
                    if ukuran != "0":
                        data['Ukuran'] = str(ukuran)
                        break
                    else:
                        print("Ukuran tidak boleh 0!")
                else:
                    print("Ukuran tidak boleh kosong. Masukkan data kembali!")

            while True:
                harga = input("Masukkan Harga baru (Rp): ")
                if harga.isdigit():
                    harga = int(harga)
                    if harga > 0:
                        data['Harga (Rp)'] = int(harga)
                        break
                    else:
                        print("Harga harus lebih besar dari 0. Masukkan data kembali!")
                else:
                    print("Masukkan angka yang valid. Masukkan data kembali!")
                
            with open("data_pestisida.csv", mode="w", newline="") as data_pestisida:
                header = ['Nama', 'Stok', 'Ukuran', 'Harga (Rp)', 'Terjual']
                writer = csv.DictWriter(data_pestisida, fieldnames=header)
                writer.writeheader()
                writer.writerows(list_pestisida)

            tampilkan_stok()
            print("Data pestisida berhasil diupdate!")
            print("-" * 68)
        else:
            input("Pilih data yang tersedia!. Klik ENTER untuk kembali!")
            update_stok()
    else:
        print("Pilihan berupa angka!")
        input("Klik ENTER untuk kembali!")
        update_stok()

    input("Klik ENTER untuk kembali!")
    pestisida()

# Fungsi untuk menghapus stok pestisida
def hapus_stok():
    clear()
    tampilkan_stok()
    
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
                
                confirm = input(f"Apakah Anda yakin ingin menghapus? [y/n] : ")
                if confirm.lower() == "y":
                    list_stok.pop(no_produk - 1)
                    with open("data_pestisida.csv", mode="w", newline="") as data_pestisida:
                        header = ['Nama', 'Stok', 'Ukuran', 'Harga (Rp)', 'Terjual']
                        writer = csv.DictWriter(data_pestisida, fieldnames=header)
                        writer.writeheader()
                        writer.writerows(list_stok)
                    tampilkan_stok()
                else:
                    pestisida()
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