import os # Mengimpor modul os untuk berinteraksi dengan sistem operasi
import csv # Mengimpor modul csv untuk membuat file csv

# Fungsi untuk  menampilkan header / judul program
def heading():
    print("="*60)
    print("A G R O S I D A".center(60))
    print("Hama Hilang, Petani Aman".center(60))
    print("="*60)

# Fungsi untuk menghapus terminal sebelum menampilkan menu baru
def clear():
    os.system('cls')

# Fungsi untuk mendaftarkan user baru
def register(): 
    clear()
    heading()
    print("REGISTER".center(60))
    print("-"*60)
    username = input("Masukkan Username: ")
    password = str(input("Masukkan Password: "))
    print("="*60)
    
    # Menambahkan data user ke dalam file csv
    with open("data_user.csv", mode="a", newline='') as file:
        header = ['username', 'password']
        writer = csv.DictWriter(file, fieldnames=header)
        if file.tell() == 0 : #Menulis header jika file masih kosong
            writer.writeheader()
        #Menulis data dari inputan user ke dalam file csv
        writer.writerow({'username': username, 'password': password})
    input("REGISTRASI Berhasil. Klik ENTER Untuk Melanjutkan!")
    start()
    
    if 

# Fungsi untuk login 
def login():
    clear()
    heading()
    print("LOGIN".center(60))
    print("-"*60)
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    print("="*60)
    
    # Membaca data user dari file csv
    with open("data_user.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                input("Login Berhasil. Klik \"ENTER\" Untuk Melanjutkan!")
                return
            
        # Menampilkan pesan jika user salah menginputkan username atau password  
        print("Username atau Password Salah. Silahkan Coba Lagi!")
        kesempatan = 1
        # Memberikan 3 kali kesempatan untuk user melakukan login jika salah input username atau password
        while kesempatan < 3:
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            
            # Membaca data user dari file csv
            with open("data_user.csv", mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'] == username and row['password'] == password:
                        input("Login Berhasil. Klik ENTER Untuk Melanjutkan!")
                        return
                 
            print("-"*60)
            print("Username atau Password Salah.")
            kesempatan += 1
        input(f"Anda telah salah input {kesempatan} kali. Klik [ENTER] untuk Regisrasi Ulang!")
        start()
        
def start():
    clear()
    heading()
    print("Silahkan Pilih Opsi Berikut!\n")
    print("[1] Login\n")
    print("[2] Register")
    print("="*60)
    option = int(input("Masukkan Pilihan: "))
    if option == 1:
        login()
    elif option == 2:
        register()
    else:
        print("Pilihan INVALID. Pilih Opsi Yang Tersedia!")
        
start()