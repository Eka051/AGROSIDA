import os
import csv
import pandas as pd

def clear():
    os.system('cls')
    
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


def beli_pestisida():
    os.system('cls')
    df = pd.read_csv("data_pestisida.csv")
    df.index = range(1, len(df) + 1)
    
    print("="*58)
    print("PRODUK PESTISIDA".center(58))
    print("-"*58)
    print(df)
    print("="*58)
    
    option = input("Pilih nomor untuk membeli produk: ")

    # Check if the input is a valid number
    if option.isdigit(): # and 1 <= int(option) <= len(df):
        selected_index = int(option)
        selected_product = df.loc[selected_index]
        jumlah_pembelian = int(input(f"Masukkan jumlah pembelian {selected_product['Nama']}: "))

        if jumlah_pembelian <= selected_product['Jumlah']:
            # Update Jumlah in the product DataFrame
            df.at[selected_index, 'Jumlah'] -= jumlah_pembelian
            df.to_csv("data_pestisida.csv", index=False)

            # Save the transaction to the history CSV file
            transaksi_df = pd.DataFrame({
                'Nama': [selected_product['Nama']],
                'Jumlah Pembelian': [jumlah_pembelian],
                'Total Harga': [jumlah_pembelian * selected_product['Harga']],
                'Tanggal Transaksi': [pd.to_datetime('today').strftime('%Y-%m-%d')]
            })

            # Append to the transaction history file
            transaksi_df.to_csv("transaksi.csv", mode='a', header=not os.path.exists("transaksi.csv"), index=False)

            # Generate and save the receipt
            save_receipt(selected_product, jumlah_pembelian)
            
            print("Transaksi berhasil. Terima kasih!")
        else:
            print("Stok tidak mencukupi. Silakan coba lagi dengan jumlah yang lebih kecil.")
    else:
        print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")

def save_receipt(selected_product, jumlah_pembelian):
    os.system('cls')
    total_harga = jumlah_pembelian * selected_product['Harga']
    receipt = f"""
    =====================================================
                            AGROSIDA
                    Hama Hilang, Petani Aman
    -----------------------------------------------------
                    STRUK PEMBELIAN PESTISIDA
    -----------------------------------------------------
    Tanggal       : {pd.to_datetime('today').strftime('%d-%M-%Y')}
    
    Nama          : {selected_product['Nama']}
    Jumlah        : {jumlah_pembelian}
    Harga Satuan  : {selected_product['Harga']}
    Total Harga   : {total_harga}
    -----------------------------------------------------
    Terima kasih telah membeli produk pestisida!
    =====================================================
    """

    # receipt_filename = f"struk_{pd.to_datetime('today').strftime('%Y%m%d%H%M%S')}.txt"

    # with open(receipt_filename, 'w') as receipt_file:
    #     receipt_file.write(receipt)

    print(receipt)
    # Function untuk transaksi pestisida
    
    
beli_pestisida()