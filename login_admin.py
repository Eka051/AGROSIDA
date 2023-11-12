import os
import csv
import pandas as pd
import getpass

def clear():
    os.system('cls')
    
def heading():
    print("="*60)
    print("A G R O S I D A".center(60))
    print("Hama Hilang, Petani Aman".center(60))
    print("="*60)
    
def login():
    clear()
    heading()
    print("LOGIN ADMIN".center(60))
    print("-"*60)
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    print("="*60)

    # Membaca data dari file csv
    data_account = [] # menyimpan data akun yang dibaca dari file csv
    with open("data_admin.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_account.append(row)

    data_login = [] # menyimpan data akun yang sesuai dengan username dan password yang dimasukkan oleh admin
    for data in data_account:
        if username == data['username'] and password == data['password']:
            data_login.append(data)
            input("Login Berhasil. Klik \"ENTER\" Untuk Melanjutkan!")
            return

    # Menampilkan pesan jika admin salah menginputkan username atau password
    print("Username atau Password Salah. Silahkan Coba Lagi!")
    print("-"*60)
    kesempatan = 1
    # Memberikan 3 kali kesempatan untuk admin melakukan login jika salah input username atau password
    while kesempatan < 3:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        for row in data_account:
            if row['username'] == username and row['password'] == password:
                print("="*60)
                input("Login Berhasil. Klik ENTER Untuk Melanjutkan!")
                return
            
        print("-"*60)
        print("Username atau Password Salah.")
        kesempatan += 1

    print(f"Anda telah salah input {kesempatan} kali. Masukkan akun admin dengan benar!")
    input("Klik ENTER untuk kembali!")
    start()
    
# Function ubah password admin dengan autentifikasi password lama
def ubah_password():
    clear()
    heading()
    print("UBAH PASSWORD ADMIN".center(60))
    print("-" * 60)

    # Membaca data admin yang tersimpan di file csv
    with open("data_admin.csv", mode="r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    username = input("Masukkan username admin: ")
    old_password = input("Masukkan password lama: ")
    
    success = False
    for admin in data:
        if username == admin['username'] and old_password == admin['password']:
            new_password = input("Masukkan password baru: ")
            admin['password'] = new_password
            success = True
            print("-"*60)
            print("Password berhasil diubah.")
            break

    if not success:
        print("-"*60)
        print("Username atau password lama salah. Gagal mengubah password.")
        input("Klik ENTER untuk kembali!")
        start()

    # Menyimpan perubahan ke file csv
    with open("data_admin.csv", mode="w", newline="") as file:
        fieldnames = ['username', 'password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    input("Klik ENTER untuk kembali login!")
    start()
    
def start():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}  
    |{"Halaman Login Admin".center(58)}|
    |{"-"*58}|
    |{"[1]. Login Admin".ljust(58)}|
    |{"[2]. Ubah Password".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Pilih Opsi: ")
    if option == "1":
        login()
    elif option == "2":
        ubah_password()
    else:
        input("Pilihan INVALID. Klik ENTER untuk kembali")
        start()
        
start() 
