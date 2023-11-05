import os # Mengimpor modul os untuk berinteraksi dengan sistem operasi
import csv # Mengimpor modul csv untuk membuat file csv

# # Fungsi untuk menampilkan header / judul program
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
    password = input("Masukkan Password: ")
    print("="*60)

    data_account = []
    # Membaca data user dari file csv
    with open("data_user.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_account.append(row)
            
    # Mengecek jika inputan user sama dengan username yang telah terdaftar
    user_ready = False
    for account in data_account:
        if username == account['username']:
            input("Username telah terdaftar. Masukkan username lain!")
            user_ready = True
            register()
            
    # Jika akun user belum terdaftar, maka akan menambahkan datanya ke dalam file csv
    if user_ready == False :
        new_account = {'username': username, 'password': password}
        with open("data_user.csv", mode="a", newline='') as file:
            header = ['username', 'password']
            writer = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(new_account)
        input("REGISTRASI Berhasil. Klik ENTER untuk ke menu selanjutnya!")
        start()

# Fungsi untuk login
def login():
    clear()
    heading()
    print("LOGIN".center(60))
    print("-"*60)
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    print("="*60)

    # Membaca data dari file csv
    data_account = [] # menyimpan data akun yang dibaca dari file csv
    with open("data_user.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_account.append(row)

    data_login = [] # menyimpan data akun yang sesuai dengan username dan password yang dimasukkan oleh user
    for data in data_account:
        if username == data['username'] and password == data['password']:
            data_login.append(data)
            input("Login Berhasil. Klik \"ENTER\" Untuk Melanjutkan!")
            return

    # Menampilkan pesan jika user salah menginputkan username atau password
    print("Username atau Password Salah. Silahkan Coba Lagi!")
    kesempatan = 1
    # Memberikan 3 kali kesempatan untuk user melakukan login jika salah input username atau password
    while kesempatan < 3:
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        for row in data_account:
            if row['username'] == username and row['password'] == password:
                input("Login Berhasil. Klik ENTER Untuk Melanjutkan!")
                return

        print("-"*60)
        print("Username atau Password Salah.")
        kesempatan += 1

    input(f"Anda telah salah input {kesempatan} kali. Klik [ENTER] untuk Registrasi Ulang!")
    start()

# Fungsi menu utama ketika program dijalankan
def start():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}  
    |{"Silahkan Pilih Opsi Berikut".center(58)}|
    |{"-"*58}|
    |{"[1]. Login".ljust(58)}|
    |{"[2]. Register".ljust(58)}|
    {'='*60}
    ''')
    option = input("Masukkan Pilihan: ")
    if option == "1":
        login()
    elif option == "2":
        register()
    else:
        input("Pilihan INVALID. Pilih Opsi Yang Tersedia!")
        start()

start()