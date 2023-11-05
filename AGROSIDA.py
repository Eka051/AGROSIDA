import os

def clear():
    os.system('cls')

def tampilan_utama():
    clear()
    print(f'''
    {"="*60}
    |{"A G R O S I D A".center(58)}|
    |{"Hama Hilang, Petani Aman".center(58)}|
    {'='*60}  
    |{"Dashboard Login".center(58)}|
    |{"-"*58}|
    |{"[1]. Login Admin".ljust(58)}|
    |{"[2]. Login User".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Masukkan Pilihan: ")
    if option == "1":
        import admin
    elif option == "2":
        import user
    else:
        input("Pilihan INVALID. Klik ENTER untuk memilih kembali!")
        tampilan_utama()
        
tampilan_utama()