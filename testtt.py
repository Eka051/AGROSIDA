import pandas as pd
import os
import csv

def clear():
    os.system('cls')

def tampilkan_stok():
    clear()
    df = pd.read_csv("data_pestisida.csv")
    df['Terjual'] = df['Terjual'].astype('int')
    df.index = range(1, len(df) + 1)

    # Menentukan lebar kolom
    col_widths = {
        "No": 3,
        "Nama": 28,
        "Jumlah": 8,
        "Ukuran": 5,
        "Harga (Rp)": 10,
        "Terjual": 10
    }

    # Menambah kolom 'Nomor'
    df.insert(0, 'No', range(1, len(df) + 1))

    # Menampilkan header
    print("="*77)
    print(f'|{"DATA STOK PESTISIDA".center(75)}|')
    print("-"*77)
    print("|" + "|".join(f"{col.center(col_widths[col] + 1)}" for col in df.columns) + "|")
    print("|" + "|".join("-" * (col_widths[col] + 1) for col in df.columns) + "|")

    # Menampilkan data
    for _, row in df.iterrows():
        row_str = f"|{str(row['No']).center(col_widths['No'] + 1)}"  # No kolom rata tengah
        row_str += f"|{str(row['Nama']).ljust(col_widths['Nama'] + 1)}"  # Nama kolom rata kiri
        for col in df.columns[2:]:  # Kolom selanjutnya rata tengah
            row_str += f"|{str(row[col]).center(col_widths[col] + 1)}"
        print(row_str + "|")

    print("="*77)

tampilkan_stok()
