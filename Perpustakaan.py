# ================================================ DATA ==================================================
id_Buku       = ['101', '102', '103']
nama_Buku     = ['Bahasa Indonesia', 'Kewarganegaraan', 'Ilmu Pengetahuan Alam']
jenis_Buku    = ['Pendidikan', 'Pendidikan', 'Pendidikan']
jumlah_Total  = [10, 20, 30]
jumlah_Pinjam = [5, 10, 20]

dataPerpustakaan = {
    'id'            : id_Buku,
    'nama'          : nama_Buku,
    'jenis'         : jenis_Buku,
    'jumlahTotal'   : jumlah_Total,
    'jumlahPinjam'  : jumlah_Pinjam
    }

# ============================================= TAMPILAN MENU =============================================
def menuUtama():
    print('''
    ===== INFORMASI DATA BUKU PERPUSTAKAAN =====''')
    print('''
    1. Data Peminjaman Buku
    2. Menambahkan Data Peminjam
    3. Update Data Peminjam
    4. Hapus Data Peminjam
    5. Keluar
    ''')

def menuMenampilkan():
    print('''
    ===MENU DATA PEMINJAM BUKU===''')
    print('''
    1. Menampilkan Semua Data
    2. Mencari Data 
    3. Kembali Ke Menu Utama
    ''')

def menuMenambahkan():
    print('''
    ===MENU MENAMBAHKAN DATA PEMINJAM BUKU===''')
    print('''
    1. Menambahkan Data Peminjam
    2. Kembali Ke Menu Utama
    ''')

def menuEdit():
    print('''
    ===MENU EDIT DATA PEMINJAM BUKU===''')
    print('''
    1. Edit Data Peminjam
    2. Kembali Ke Menu Utama
    ''')

def menuHapus():
    print('''
    ===MENU HAPUS DATA PEMINJAM BUKU===''')
    print('''
    1. Hapus Data Peminjam 
    2. Kembali Ke Menu Utama
    ''')

# ================================================ FUNGSI ================================================
def menampilkanData():                                                                 # Menampilkan Data
    judul = ['ID', 'NAMA', 'JENIS', 'JUMLAH TOTAL', 'JUMLAH PINJAM']
    print(f'''
    {judul[0]:<25}{judul[1]:<25}{judul[2]:<25}{judul[3]:<25}{judul[4]:}''')
    print('======================================================================================================================================')

    for i in range(len(id_Buku)):
        for j in range(len(list(dataPerpustakaan.keys()))):
            hasil = list(dataPerpustakaan.values())[j][i]
            print('{:<27}'.format(hasil),end ='')
        print() 

def mencariData(j):                                                                    # Mencari Data
    pencarianData = input('Masukkan ID Buku: ')
    if pencarianData in id_Buku:
        indexPencarian = id_Buku.index(pencarianData)
        judul = ['ID', 'NAMA', 'JENIS', 'JUMLAH TOTAL', 'JUMLAH PINJAM']
        print(f'''
        {judul[0]: <25}{judul[1]: <25}{judul[2]: <25}{judul[3]: <25}{judul[4]:}''')
        print('======================================================================================================================================')
        for j in range(len(list(dataPerpustakaan.keys()))):
            hasil = list(dataPerpustakaan.values())[j][indexPencarian]
            print('{:<27}'.format(hasil), end ='')
        print() 
    else:
        print('Data Tidak Ditemukan')
            
def masukanData():                                                                     # Menambahkan Data
    masuk_ID = input('Masukkan ID Buku: ')
    if masuk_ID in id_Buku:
        print('ID sudah digunakan ')
    else:
        masuk_Nama = input('Masukkan Nama Buku: ')
        masuk_Jenis = input('Masukkan Jenis Buku: ')
        masuk_Total = input('Masukkan Jumlah Buku Keseluruhan: ')
        masuk_Pinjam = input('Masukkan Jumlah Buku yang Terpinjam: ')
        if masuk_Total.isnumeric() and masuk_Pinjam.isnumeric():
            masuk_Total = int(masuk_Total)
            masuk_Pinjam = int(masuk_Pinjam)
            if masuk_Total > masuk_Pinjam:
                simpan_Data = input('Apakah Mau Menambahkan Data?(y/n): ')
                if simpan_Data == 'y':
                    id_Buku.append(masuk_ID)
                    nama_Buku.append(masuk_Nama)
                    jenis_Buku.append(masuk_Jenis)
                    jumlah_Total.append(masuk_Total)
                    jumlah_Pinjam.append(masuk_Pinjam)
                    print('Data Berhasil Tersimpan')
                elif simpan_Data == 'n':
                    print('Batal Menyimpan Data')
                else:
                    print('Pilihan Salah. Harap Masukkan y/n Sebagai Yes/No')
            else:
                print('Jumlah Buku yang Di Pinjam Lebih Banyak Dari Jumlah Stok Buku')
        else:
            print('Jumlah Buku Harus Berupa Angka')    

def editData():                                                                        # Mengedit Data
    menampilkanData()
    print()
    pencarianData = input('Masukkan ID Buku Yang Ingin Di Edit: ')
    if pencarianData in id_Buku:
        indexEdit = id_Buku.index(pencarianData)
        judul = ['ID', 'NAMA', 'JENIS', 'JUMLAH TOTAL', 'JUMLAH PINJAM']
        print(f'''
        {judul[0]: <25}{judul[1]: <25}{judul[2]: <25}{judul[3]: <25}{judul[4]:}''')
        print('======================================================================================================================================')
        for j in range(len(list(dataPerpustakaan.keys()))):
            hasil = list(dataPerpustakaan.values())[j][indexEdit]
            print('{:<27}'.format(hasil), end ='')
        print()
        print()
        notifEdit = input('Apakah Yakin Untuk Edit Data?(y/n): ')
        if notifEdit == 'y':
            edit_Nama = input('Masukkan Nama Baru: ')
            edit_Jenis = input('Masukkan Jenis Buku: ')
            edit_Total = input('Masukkan Jumlah Buku Keseluruhan: ')
            edit_Pinjam = input('Masukkan Jumlah Buku Yang Terpinjam: ')
            if edit_Total.isnumeric() and edit_Pinjam.isnumeric():
                edit_Total = int(edit_Total)
                edit_Pinjam = int(edit_Pinjam)
                endEdit = input('Apakah Yakin Utuk Menyimpan Data Baru?(y/n): ')
                if endEdit == 'y':
                    nama_Buku[indexEdit] = edit_Nama
                    jenis_Buku[indexEdit] = edit_Jenis
                    jumlah_Total[indexEdit] = edit_Total
                    jumlah_Pinjam[indexEdit] = edit_Pinjam

                    menampilkanData()
                elif endEdit == 'n':
                    print('Data Batal Di Simpan')
                else:
                    print('Pilihan Salah. Harap Masukkan Y/N Sebagai Yes/No')              
            else:
                print('Jumlah Buku Harus Berupa Angka')
        elif notifEdit == 'n':
            print('Batal Edit Data')  
        else:
            print('Pilihan Salah. Harap Masukkan y/n Sebagai Yes/No')

    else:
        print('Data Tidak Ditemukan')

def hapusData():                                                                       # Menghapus Data
    menampilkanData()
    print()
    hapus = input('Silahkan Masukan ID Buku yang Ingin Di Hapus: ')
    if hapus in id_Buku:
        notifHapus = input('Apakah Anda Yakin Untuk Menghapus Data Buku(Y/N): ')
        if notifHapus == 'y':
            index_IdBuku = id_Buku.index(hapus)
            id_Buku.pop(index_IdBuku)
            nama_Buku.pop(index_IdBuku)
            jenis_Buku.pop(index_IdBuku)
            jumlah_Total.pop(index_IdBuku)
            jumlah_Pinjam.pop(index_IdBuku)
            print('Data Buku Berhasil Di Hapus')
        elif notifHapus == 'n':
            print('Data Buku Batal Di Hapus')
        else:
            print('Pilihan Salah. Harap Masukkan Y/N Sebagai Yes/No')
    else:
        print('ID yang Ingin Di Hapus Tidak Tersedia')

# ================================================ PROGRAM ================================================
while True:
    menuUtama()
    pilihMenu = input('Masukkan Angka Sesuai Menu [1-5]: ')

    if pilihMenu == '1':                                                               # Menampilkan Menu Data Peminjaman Buku
        while True:
            menuMenampilkan()
            Data = input('Silahkan Pilih Menu: ')       
            if Data == '1':
                menampilkanData()
            elif Data == '2':
                mencariData(Data)
            else:
                break
                                   
    elif pilihMenu == '2':                                                             # Menampilkan Menu Menambahkan Data Peminjam
        while True:
            menuMenambahkan()
            Tambah = input('Silahkan Pilih Menu: ')
            if Tambah == '1':
                masukanData()
            else:
                break
        
    elif pilihMenu == '3':                                                             # Menampilkan Menu Edit Data Peminjam
        while True:
            menuEdit()
            Edit = input('Silahkan Pilih Menu: ')
            if Edit == '1':
                editData()
            else:
                break

    elif pilihMenu == '4':                                                             # Menampilkan Menu Hapus Data Peminjam
        while True:
            menuHapus()
            Hapus = input('Silahkan Pilih Menu: ')
            if Hapus == '1':
                hapusData()
            else:
                break

    elif pilihMenu == '5':                                                             # Keluar dari program
        exit()
    else:                                                                              # Menampilkan Menu Utama Jika Salah Input Angka
        print('Masukan Angka Sesuai Menu')