import csv
import os
import pandas as pd

def clear():
    os.system('cls')

def entri_info():
    clear()

    with open("info_tanaman.csv", mode="a", newline="") as info_tanaman:
        header = ['Nama', 'Hama', 'Pestisida', 'Dosis']
        writer = csv.DictWriter(info_tanaman, fieldnames=header)

        # Menulis header hanya jika belum ada dalam file CSV
        if info_tanaman.tell() == 0:
            writer.writeheader()

        print("=" * 60)
        print("ENTRI INFO TANAMAN".center(60))
        print("-" * 60)

        counter = True
        while counter:
            nama = input("Masukkan nama tanaman: ")

            # Input hama
            hama_list = []
            pestisida_list = []
            dosis_list = []
            while True:
                hama = input("Masukkan hama tanaman: ")

                # Input pestisida dan dosis untuk setiap hama
                while True:
                    pestisida = input(f"Masukkan pestisida untuk {hama}: ")
                    dosis = input(f"Masukkan dosis {pestisida}: ")

                    pestisida_list.append(pestisida)
                    dosis_list.append(dosis)
                    print("-"*60)
                    option = input("Tambah pestisida dan dosis lagi? [y/n]: ")
                    if option.lower() != "y":
                        break

                hama_list.append(hama)
                print("-"*60)
                option = input("Tambah hama lagi? [y/n]: ")
                if option.lower() != "y":
                    break

            # Menulis data ke dalam file CSV dalam format yang diinginkan
            writer.writerow({'Nama': nama, 'Hama': hama_list, 'Pestisida': pestisida_list, 'Dosis': dosis_list})
            print("-"*60)
            option = input("Tambah data lagi? [y/n]: ")
            if option.lower() == "y":
                counter = True
            else:
                counter = False

        print("\nData telah ditambahkan ke dalam file CSV.")
        
print("="*60)
df = pd.read_csv("info_tanaman.csv")
print(df)

# Contoh penggunaan
entri_info()
