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
    
    option = input("Pilih nomor untuk membeli produk: ")

    if option.isdigit() and 1 <= int(option) <= len(df):
        selected_index = int(option)
        selected_product = df.loc[selected_index]
        jumlah_pembelian = int(input(f"Masukkan jumlah pembelian {selected_product['Nama']}: "))

        if jumlah_pembelian <= selected_product['Jumlah']:
            # Update Jumlah pestisida di file csv
            df.at[selected_index, 'Jumlah'] -= jumlah_pembelian
            df.to_csv("data_pestisida.csv", index=False)

            # Menyimpan data transaksi ke file csv
            transaksi_df = pd.DataFrame({
                'Nama Produk': [selected_product['Nama']],
                'Jumlah Pembelian': [jumlah_pembelian],
                'Total Harga': [jumlah_pembelian * selected_product['Harga (Rp)']],
                'Tanggal Transaksi': [pd.to_datetime('today').strftime('%d-%m-%Y')]
            })

            # Menambahkan data transaksi ke dalam file transaksi.csv
            transaksi_df.to_csv("transaksi.csv", mode='a', header=not os.path.exists("transaksi.csv"), index=False)
                    
            # Untuk mencetak struk dari pembelian user
            save_receipt(selected_product, jumlah_pembelian)
            
            input("Transaksi berhasil. Klik ENTER untuk kembali!")
            main_menu()
        else:
            input("Stok tidak mencukupi. Silakan coba lagi dengan jumlah yang lebih kecil.")
            beli_pestisida()
    else:
        input("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")
        beli_pestisida()

def save_receipt(selected_product, jumlah_pembelian):
    clear()
    total_harga = jumlah_pembelian * selected_product['Harga (Rp)']
    receipt = f"""
    =====================================================
                            AGROSIDA
                    Hama Hilang, Petani Aman
    -----------------------------------------------------
                    STRUK PEMBELIAN PESTISIDA
    -----------------------------------------------------
    Tanggal       : {pd.to_datetime('today').strftime('%d-%m-%Y')}
    
    Nama Produk   : {selected_product['Nama']}
    Jumlah        : {jumlah_pembelian}
    Harga Satuan  : {selected_product['Harga (Rp)']}
    -----------------------------------------------------
    Total Harga   : {total_harga}
    
    Terima kasih telah membeli produk pestisida!
    =====================================================
    """
    print(receipt)
    
    
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
    |{"[3]. Exit".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Pilih Opsi: ")
    if option == "1":
        info_tanaman()
    elif option == "2":
        beli_pestisida()
    elif option == "3":
        exit()
    else:
        input("Pilihan INVALID. Pilih Opsi Yang Tersedia!")
        main_menu()
        
main_menu()