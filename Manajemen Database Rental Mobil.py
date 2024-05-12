import regex as re
import sys
from datetime import datetime, timedelta
from tabulate import tabulate


## Kumpulan Pattern

alnumPattern = r'^[a-zA-Z0-9\s]*$'
yearPattern = r'^\d{4}$'
platePattern = r'^[A-Z]{1,2}\s{1}\d{1,4}\s{1}[A-Z]{0,3}$'
alphaPattern = r'^[a-zA-Z]*$'
emailPattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
phonePattern = r'^0[0-9]{9,11}$'
ktpPattern = r'^[0-9]{16}$'
datePattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])' 
cusIDPattern = r'^P[1-9]{1}[0-9]{1,2}'
carIDPattern = r'^M[1-9]{1}[0-9]{1,2}'


## Kumpulan Header

cusHeader = ['ID', 'Nama', 'e-mail', 'Telefon', 'KTP']
carHeader = ['ID', 'Model', 'Tahun', 'Plat', 'Kategori', 'Tipe']
rentHeader = ['ID', 'ID Mobil', 'ID Pelanggan', 'Awal Sewa', 'Akhir Sewa']


## Kumpulan Function Display

def displayMenu():
    print("\nMenu:")
    print("1. Input Data")
    print("2. Lihat Data")
    print("3. Lihat Data Sorted")
    print("4. Ubah Data")
    print("5. Hapus Data")
    print("6. Keluar")

def displayDataChoice():
    print("\nMenu Pilihan Data:")
    print("1. Data Pelanggan")
    print("2. Data Mobil")
    print("3. Data Sewa")
    print("4. Menu Utama")

def displayReadChoice():
    print("\nMenu:")
    print("1. Data Pelanggan")
    print("2. Data Mobil")
    print("3. Data Sewa")
    print("4. Data Individu Penyewa")
    print("5. Data Individu Mobil")
    print("6. Menu Utama")


## Kumpulan Placeholder database
    
dataPelanggan = {
    'P1': {
        'Nama': 'Ahmad',
        'e-mail': 'Sahmad@example.com',
        'Telefon': '081234567890',
        'KTP': '1234567890123456'
    },
    'P2': {
        'Nama': 'Budi',
        'e-mail': 'Sbudi@example.com',
        'Telefon': '081234567891',
        'KTP': '2345678901234567'
    },
    'P3': {
        'Nama': 'Zubidan',
        'e-mail': 'Schandra@example.com',
        'Telefon': '081234567892',
        'KTP': '3456789012345678'
    },
    'P4': {
        'Nama': 'Dewi',
        'e-mail': 'Sdewi@example.com',
        'Telefon': '081234567893',
        'KTP': '4567890123456789'
    },
    'P5': {
        'Nama': 'Endah',
        'e-mail': 'Sendah@example.com',
        'Telefon': '081234567894',
        'KTP': '5678901234567890'
    },
    'P6': {
        'Nama': 'Fahmi',
        'e-mail': 'Sfahmi@example.com',
        'Telefon': '081234567895',
        'KTP': '6789012345678901'
    },
    'P7': {
        'Nama': 'Agus',
        'e-mail': 'Sgita@example.com',
        'Telefon': '081234567896',
        'KTP': '7890123456789012'
    },
    'P8': {
        'Nama': 'Hadi',
        'e-mail': 'Shadi@example.com',
        'Telefon': '081234567897',
        'KTP': '8901234567890123'
    },
    'P9': {
        'Nama': 'Yohanes',
        'e-mail': 'Sindra@example.com',
        'Telefon': '081234567898',
        'KTP': '9012345678901234'
    },
    'P10': {
        'Nama': 'Joko',
        'e-mail': 'Sjoko@example.com',
        'Telefon': '081234567899',
        'KTP': '0123456789012345'
    },
}

dataMobil = {
    "M1": {
        "Model Mobil": "Toyota Avanza",
        "Tahun Pembuatan": "2019",
        "Nomor Polisi": "B 1234 AB",
        "Kategori": "Low Class",
        "Tipe Mobil": "MPV"
    },
    "M2": {
        "Model Mobil": "Honda City",
        "Tahun Pembuatan": "2018",
        "Nomor Polisi": "B 5678 CD",
        "Kategori": "Middle Class",
        "Tipe Mobil": "Sedan"
    },
    "M3": {
        "Model Mobil": "Toyota Fortuner",
        "Tahun Pembuatan": "2020",
        "Nomor Polisi": "B 9012 EF",
        "Kategori": "Middle Class",
        "Tipe Mobil": "SUV"
    },
    "M4": {
        "Model Mobil": "Nissan X-Trail",
        "Tahun Pembuatan": "2017",
        "Nomor Polisi": "B 3456 GH",
        "Kategori": "Middle Class",
        "Tipe Mobil": "SUV"
    },
    "M5": {
        "Model Mobil": "Mitsubishi Pajero Sport",
        "Tahun Pembuatan": "2019",
        "Nomor Polisi": "B 7890 IJ",
        "Kategori": "Middle Class",
        "Tipe Mobil": "SUV"
    },
    "M6": {
        "Model Mobil": "Honda CR-V",
        "Tahun Pembuatan": "2020",
        "Nomor Polisi": "B 2345 KL",
        "Kategori": "Middle Class",
        "Tipe Mobil": "SUV"
    },
    "M7": {
        "Model Mobil": "Toyota Innova",
        "Tahun Pembuatan": "2016",
        "Nomor Polisi": "B 6789 MN",
        "Kategori": "Middle Class",
        "Tipe Mobil": "MPV"
    },
    "M8": {
        "Model Mobil": "Mazda CX-5",
        "Tahun Pembuatan": "2019",
        "Nomor Polisi": "B 0123 OP",
        "Kategori": "Middle Class",
        "Tipe Mobil": "SUV"
    },
    "M9": {
        "Model Mobil": "Hyundai Tucson",
        "Tahun Pembuatan": "2018",
        "Nomor Polisi": "B 4567 QR",
        "Kategori": "Middle Class",
        "Tipe Mobil": "SUV"
    },
    "M10": {
        "Model Mobil": "Kia Seltos",
        "Tahun Pembuatan": "2021",
        "Nomor Polisi": "B 8901 ST",
        "Kategori": "Middle Class",
        "Tipe Mobil": "SUV"
    },
}

dataSewa = {
    'R1': {
        'id_mobil': 'M1', 
        'id_pelanggan': 'P10', 
        'waktu_mulai_sewa': '2024-02-01', 
        'waktu_berakhir_sewa': '2024-02-04'
        },
    'R2': {
        'id_mobil': 'M3', 
        'id_pelanggan': 'P8', 
        'waktu_mulai_sewa': '2024-02-05', 
        'waktu_berakhir_sewa': '2024-02-07'
        },
    'R3': {
        'id_mobil': 'M9', 
        'id_pelanggan': 'P3', 
        'waktu_mulai_sewa': '2024-02-08', 
        'waktu_berakhir_sewa': '2024-02-14'
        },
    'R4': {
        'id_mobil': 'M6', 
        'id_pelanggan': 'P1', 
        'waktu_mulai_sewa': '2024-02-15', 
        'waktu_berakhir_sewa': '2024-02-21'
        },
    'R5': {
        'id_mobil': 'M8', 
        'id_pelanggan': 'P2', 
        'waktu_mulai_sewa': '2024-02-22', 
        'waktu_berakhir_sewa': '2024-02-27'
        },
    'R6': {
        'id_mobil': 'M5', 
        'id_pelanggan': 'P9', 
        'waktu_mulai_sewa': '2024-02-28', 
        'waktu_berakhir_sewa': '2024-03-02'
        },
    'R7': {
        'id_mobil': 'M10', 
        'id_pelanggan': 'P7', 
        'waktu_mulai_sewa': '2024-03-03', 
        'waktu_berakhir_sewa': '2024-03-08'
           },
    'R8': {
        'id_mobil': 'M4', 
        'id_pelanggan': 'P5', 
        'waktu_mulai_sewa': '2024-03-09', 
        'waktu_berakhir_sewa': '2024-03-14'
        },
    'R9': {
        'id_mobil': 'M2', 
        'id_pelanggan': 'P10', 
        'waktu_mulai_sewa': '2024-03-15', 
        'waktu_berakhir_sewa': '2024-03-17'
        },
    'R10': {
        'id_mobil': 'M7', 
        'id_pelanggan': 'P6', 
        'waktu_mulai_sewa': '2024-03-18', 
        'waktu_berakhir_sewa': '2024-03-22'
        },
    'R11': {
        'id_mobil': 'M8', 
        'id_pelanggan': 'P9', 
        'waktu_mulai_sewa': '2024-03-23', 
        'waktu_berakhir_sewa': '2024-03-25'
        },
    'R12': {
        'id_mobil': 'M3', 
        'id_pelanggan': 'P4', 
        'waktu_mulai_sewa': '2024-03-26', 
        'waktu_berakhir_sewa': '2024-04-10'
        },
    'R13': {
        'id_mobil': 'M1', 
        'id_pelanggan': 'P3', 
        'waktu_mulai_sewa': '2024-03-31', 
        'waktu_berakhir_sewa': '2024-04-03'
        },
    'R14': {
        'id_mobil': 'M9', 
        'id_pelanggan': 'P8', 
        'waktu_mulai_sewa': '2024-04-04', 
        'waktu_berakhir_sewa': '2024-04-07'
        },
    'R15': {
        'id_mobil': 'M8', 
        'id_pelanggan': 'P6', 
        'waktu_mulai_sewa': '2024-04-08', 
        'waktu_berakhir_sewa': '2024-04-13'
        },
    'R16': {
        'id_mobil': 'M5', 
        'id_pelanggan': 'P2', 
        'waktu_mulai_sewa': '2024-04-02', 
        'waktu_berakhir_sewa': '2024-04-03'
        },
    'R17': {
        'id_mobil': 'M7', 
        'id_pelanggan': 'P1', 
        'waktu_mulai_sewa': '2024-04-20', 
        'waktu_berakhir_sewa': '2024-04-25'
        },
    'R18': {
        'id_mobil': 'M10', 
        'id_pelanggan': 'P7', 
        'waktu_mulai_sewa': '2024-04-01', 
        'waktu_berakhir_sewa': '2024-04-02'
        }
}


## Fungsi Pendukung

# Fungsi Tuple Database
def updateTuple():
    global tuplePelanggan, tupleMobil, tupleSewa
    tuplePelanggan = tuple((key, value['Nama'], value['e-mail'], value['Telefon'], value['KTP']) for key, value in dataPelanggan.items())
    tupleMobil = tuple((key, value['Model Mobil'], value['Tahun Pembuatan'], value['Nomor Polisi'], value['Kategori'], value['Tipe Mobil']) for key, value in dataMobil.items())
    tupleSewa = tuple((key, value['id_mobil'], value['id_pelanggan'], value['waktu_mulai_sewa'], value['waktu_berakhir_sewa']) for key, value in dataSewa.items())

# Fungsi untuk validasi pattern
def inputValidation(pattern, input):
    return re.match(pattern, input) is not None


## Create Functions

# Input data pelanggan
def inputDataPelanggan():
    # Nama pelanggan
    while True:
        np = input("\nMasukkan nama anda: ").capitalize()
        if inputValidation(alphaPattern, np):
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    # email pelanggan
    while True:
        em = input("\nMasukkan email anda: ").lower()
        if inputValidation(emailPattern, em):
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    # Nomor telefon pelanggan
    while True:
        hp = input("\nMasukkan nomor telefon anda: ")
        if inputValidation(phonePattern, hp):
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    # Nomor ktp pelanggan
    while True:
        ktp = input("\nMasukkan nomor KTP anda(16 digit): ")
        if inputValidation(ktpPattern, ktp):
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    newCusData = {'Nama': np,
                  'e-mail': em,
                  'Telefon': hp,
                  'KTP': ktp}
    newKey = "P" + str(len(dataPelanggan) + 1)
    dataPelanggan[newKey] = newCusData
    
# Input data mobil
def inputDataMobil():
    # Model mobil
    while True:
        mm = input("\nMasukkan model mobil, contohnya Toyota Calya atau Honda Brio: ").capitalize()
        if inputValidation(alnumPattern, mm):
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    # Tahun pembuatan
    while True:
        tp = input("\nMasukkan tahun pembuatan mobil: ")
        if inputValidation(yearPattern, tp):
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    # Nomor polisi
    while True:
        np = input("\nMasukkan nomor polisi mobil, contohnya B 1234 ABC: ").upper()
        if inputValidation(platePattern, np):
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    # Kategori
    while True:
        kt = input("\nPilih Kategori:\n1. Low class car\n2. Middle class car\n3. High class car\nMasukkan pilihan anda:  ")
        if kt == "1":
            kt = "Low Class"
            break
        elif kt == "2":
            kt = "Middle Class"
            break
        elif kt == "3":
            kt = "High Class"
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    # Tipe mobil
    while True:
        ty = input("\nPilih Tipe:\n1. Sedan\n2. MPV\n3. SUV\nMasukkan pilihan anda: ")
        if ty == "1":
            ty = "Sedan"
            break
        elif ty == "2":
            ty = "MPV"
            break
        elif ty == "3":
            ty = "SUV"
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
    newCarData = {"Model Mobil": mm,
                  "Tahun Pembuatan": tp,
                  "Nomor Polisi": np,
                  "Kategori": kt,
                  "Tipe Mobil": ty}
    newKey = "M" + str(len(dataMobil) + 1)
    dataMobil[newKey] = newCarData

# input data sewa
def inputDataSewa():

    updateTuple()

    # ID dari mobil
    while True:
        print("Model Mobil:")
        readTable(tupleMobil, carHeader)
        idM = input("\nMasukkan ID mobil, contohnya M1, M2 dst... ").capitalize()
        if idM in dataMobil:
            break
        else:
            print("ID mobil yang anda masukkan tidak ada di data kami. Mohon pilih ulang.")
            
    # ID dari pelanggan
    while True:
        print("Pelanggan:")
        readTable(tuplePelanggan,cusHeader)
        idP = input("\nMasukkan ID Pelanggan, contohnya P1, P2 dst... ").capitalize()
        if idP in dataPelanggan:
            break
        else:
            print("ID pelanggan yang anda masukkan tidak ada di data kami. Mohon pilih ulang.")
   
    # Tanggal mulai sewa
    while True:
        ms = input("\nMasukkan tanggal mulai sewa dengan format YYYY-MM-DD: ")
        if inputValidation(datePattern, ms):
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi")
   
    # Tanggal selesai sewa
    while True:
        try:
            ss = int(input("\nMasukkan jumlah hari sewa(maksimal 30 hari): "))
            if 0 < ss <= 30:
                break
            else:
                print("1Input anda tidak sesuai, silahkan coba lagi")
        except ValueError:
            print("2Input anda tidak sesuai, silahkan coba lagi")
    date_obj = datetime.strptime(ms, '%Y-%m-%d')
    
    # Add the specified number of days to the date
    new_date_obj = date_obj + timedelta(days=ss)
    
    # Convert the new datetime object back to a string
    ss = new_date_obj.strftime('%Y-%m-%d')

    newDateData = {'id_mobil': idM,
                  'id_pelanggan': idP,
                  'waktu_mulai_sewa': ms,
                  'waktu_berakhir_sewa': ss}
    newKey = "R" + str(len(dataSewa) + 1)
    dataSewa[newKey] = newDateData


## Read Functions

# Read Tables
def readTable(data, headers):
    print(tabulate(data, headers=headers, tablefmt='grid'))

# Read data sewa tiap pelanggan
def readIndCus():

    updateTuple()

    # Memberikan pilihan pelanggan
    while True:
        readTable(tuplePelanggan, cusHeader)
        idP = input("\nMasukkan ID pelanggan yang anda pilih, contohnya P1, P2 dst: ").upper()
        if idP in dataPelanggan:
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi.")

    # Mendapatkan detail pelanggan
    cusName = dataPelanggan[idP]['Nama']

    # Menyiapkan parameter tabel
    tableData = []
    for rentalID, rentalInfo in dataSewa.items():
        if rentalInfo['id_pelanggan'] == idP:
            tableData.append([rentalID, rentalInfo['id_mobil'], rentalInfo['waktu_mulai_sewa'], rentalInfo['waktu_berakhir_sewa']])

    print(f"Nama Pelanggan: {cusName}")
    print(tabulate(tableData, headers=['Rental ID', 'ID Mobil', 'Waktu Mulai Sewa', 'Waktu Berakhir Sewa'], tablefmt='grid'))
    
# Read data sewa tiap mobil
def readIndCar():

    updateTuple()

    # Memberikan pilihan customer
    while True:
        readTable(tupleMobil, carHeader)
        idM = input("\nMasukkan ID mobil yang anda pilih, contohnya M1, M2 dst: ").upper()
        if idM in dataMobil:
            break
        else:
            print("Input anda tidak sesuai, silahkan coba lagi.")
    
    # Mendapatkan detail mobil
    car_details = dataMobil[idM]
    carName = f"{idM} {car_details['Model Mobil']} {car_details['Tahun Pembuatan']}"
    
    # Menyiapkan detail tabel
    tableData = []
    for rentalID, rentalInfo in dataSewa.items():
        if rentalInfo['id_mobil'] == idM:
            tableData.append([rentalID, rentalInfo['id_mobil'], rentalInfo['waktu_mulai_sewa'], rentalInfo['waktu_berakhir_sewa']])
    
    print(f"Nama Mobil: {carName}")
    print(tabulate(tableData, headers=['Rental ID', 'ID Mobil', 'Waktu Mulai Sewa', 'Waktu Berakhir Sewa'], tablefmt='grid'))

## Sorted Table Function
    
def sortedTable(data, fieldKey):
    # Mengurutkan data berdasarkan fieldKey
    sorted_data = sorted(data.items(), key=lambda x: x[1][fieldKey])

    # membuat list dari data
    table_data = []
    for key, value in sorted_data:
        row = [key]
        row.extend(value.values())
        table_data.append(row)

    # mendefinisikan header
    headers = ["ID"] + list(data[next(iter(data))].keys())

    # membuat tabel
    return tabulate(table_data, headers=headers, tablefmt="grid")

## Update Function 
    
def updateEntry():

    updateTuple()
    
    # Pilihan database
    while True:
        displayDataChoice()
        choice = input("\nMasukkan pilihan anda: ")
        if choice == "1":
            readTable(tuplePelanggan, cusHeader)
            entryID = input(f"\nMasukkan ID pelanggan yang anda pilih: ").upper()
            if entryID in dataPelanggan:
                while True:

                    choice = input("\nPilih value yang akan anda ganti: \n1. Nama \n2. e-mail \n3. Telefon \n4. KTP \nMasukkan pilihan anda: ")
                    if choice == "1":
                        while True:
                            np = input(f"\nMasukkan nama baru untuk pelanggan {entryID}: ").capitalize()
                            if inputValidation(alphaPattern, np):
                                dataPelanggan[entryID]['Nama'] = np
                                break
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")
                        break

                    elif choice == "2":
                        while True:
                            em = input(f"\nMasukkan e-mail baru untuk pelanggan {entryID}: ").lower()
                            if inputValidation(emailPattern, em):
                                dataPelanggan[entryID]['e-mail'] = em
                                break      
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")                  
                        break

                    elif choice == "3":
                        while True:
                            hp = input(f"\nMasukkan nomor telefon baru untuk pelanggan {entryID}: ")
                            if inputValidation(phonePattern, hp):
                                dataPelanggan[entryID]['Telefon'] = hp
                                break      
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")                  
                        break

                    elif choice == "4":
                        while True:
                            ktp = input(f"Masukkan nomor ktp baru untuk pelanggan {entryID}(16 digit): ")
                            if inputValidation(ktpPattern, ktp):
                                dataPelanggan[entryID]['KTP'] = ktp
                                break      
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")                  
                        break

                    else:
                        print("Input anda tidak sesuai, silahkan coba lagi")

                break

        elif choice == "2":
            readTable(tupleMobil, carHeader)
            entryID = input(f"Masukkan ID mobil yang anda pilih: ").upper()
            if entryID in dataMobil:
                while True:

                    choice = input("\nPilih value yang akan anda ganti: \n1. Model mobil \n2. Tahun \n3. Nomor polisi \n4. Kategori \n5. Tipe mobil \nMasukkan pilihan anda: ")
                    
                    if choice == "1":
                        while True:
                            mm = input(f"Masukkan model baru untuk mobil {entryID}: ").capitalize()
                            if inputValidation(alnumPattern, mm):
                                dataMobil[entryID]['Model Mobil'] = mm
                                break
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")
                        break
                    
                    elif choice == "2":
                        while True:
                            tp = input(f"Masukkan tahun pembuatan baru untuk mobil {entryID}: ")
                            if inputValidation(yearPattern, tp):
                                break
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")
                        break
                    
                    elif choice == "3":
                        while True:
                            np = input(f"Masukkan nomor polisi baru untuk mobil {entryID}, contohnya B 1234 ABC: ").upper()
                            if inputValidation(platePattern, np):
                                break
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")
                        break
                    
                    elif choice == "4":
                        while True:
                            kt = input("Pilih Kategori:\n1. Low class car\n2. Middle class car\n3. High class car\nMasukkan pilihan anda:  ")
                            if kt == "1":
                                kt = "Low Class"
                                break
                            elif kt == "2":
                                kt = "Middle Class"
                                break
                            elif kt == "3":
                                kt = "High Class"
                                break
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")
                        dataMobil[entryID]['Kategori'] = kt
                        
                        break
                    
                    elif choice == "5":
                        while True:
                            ty = input("Pilih Kategori:\n1. Sedan\n2. MPV\n3. SUV\nMasukkan pilihan anda: ")
                            if ty == "1":
                                ty = "Sedan"
                                break
                            elif ty == "2":
                                ty = "MPV"
                                break
                            elif ty == "3":
                                ty = "SUV"
                                break
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")
                        dataMobil[entryID]['Tipe Mobil'] = ty
                        
                        break
                    
                    else:
                        print("Input anda tidak sesuai, silahkan coba lagi")
                
                break

        elif choice == "3":
            readTable(tupleSewa, rentHeader)
            entryID = input(f"Masukkan ID sewa yang anda pilih: ").upper()
            if entryID in dataSewa:

                while True:
                    choice = input("\nPilih value yang akan anda ganti: \n1. ID mobil \n2. ID pelanggan \n3. Tanggal sewa \nMasukkan pilihan anda:  ")
                    
                    if choice == "1":
                        dataSewa[entryID]['id_mobil'] = input(f"Masukkan ID mobil baru untuk sewa {entryID}: ")
                        break
                    
                    elif choice == "2":
                        dataSewa[entryID]['id_pelanggan'] = input(f"Masukkan ID pelanggan baru untuk sewa {entryID}: ")
                        break
                    
                    elif choice == "3":
                        while True:
                            ms = input("Masukkan tanggal mulai sewa dengan format YYYY-MM-DD: ")
                            if inputValidation(datePattern, ms):
                                ss = int(input("Masukkan jumlah hari sewa(maksimal 30 hari): "))
                                if 0 < ss <= 30:
                                    break
                                break
                            else:
                                print("Input anda tidak sesuai, silahkan coba lagi")
                        date_obj = datetime.strptime(ms, '%Y-%m-%d')
    
                        new_date_obj = date_obj + timedelta(days=ss)
                        
                        ss = new_date_obj.strftime('%Y-%m-%d')
                        dataSewa[entryID]['waktu_mulai_sewa'] = ms
                        dataSewa[entryID]['waktu_berakhir_sewa'] = ss
                        break
                    else:
                        print("Input anda tidak sesuai, silahkan coba lagi")

                break

        elif choice == "4":
            main()
        else:
            print("Input anda salah, silahkan coba lagi.")
    
    print("berhasil diubah")


## Delete Function

def deleteEntry():

    updateTuple()
    
    # Pilihan database
    while True:
        displayDataChoice()
        choice = input("Masukkan pilihan anda: ")
        if choice == "1":
            readTable(tuplePelanggan, cusHeader)
            database = dataPelanggan
            x = "pelanggan"
            break
        elif choice == "2":
            readTable(tupleMobil, carHeader)
            database = dataMobil
            x = "mobil"
            break
        elif choice == "3":
            readTable(tupleSewa, rentHeader)
            database = dataSewa
            x = "sewa"
            break
        elif choice == "4":
            main()
        else:
            print("Input anda salah, silahkan coba lagi.")
    
    # Cek untuk ID dan delete
    while True:
        entryID = input(f"Masukkan ID {x} yang anda pilih: ").upper()
        if entryID in database:
            del database[entryID]
            break
        else:
            print("Input anda salah, silahkan coba lagi.")


## Main Interface

def main():
    while True:
        print("\nMain")
        displayMenu()
        choice = input("\nMasukkan Pilihan Anda: ")

        ## Create Choice
        if choice == "1":
            while True:
                print("\nInput")
                displayDataChoice()
                choice = input("\nMasukkan Pilihan Anda: ")
                if choice == "1":
                    inputDataPelanggan()
                    updateTuple()
                    readTable(tuplePelanggan, cusHeader)
                    
                elif choice == "2":
                    inputDataMobil()
                    updateTuple()
                    readTable(tupleMobil, carHeader)
                    
                elif choice == "3":
                    inputDataSewa()
                    updateTuple()
                    readTable(tupleSewa, rentHeader)
                    
                elif choice == "4":
                    main()

                else:
                    print("Input anda salah, silahkan coba lagi.")

        ## Read Choice
        elif choice == "2":
            while True:
                print("\nRead")
                displayReadChoice()
                choice = input("\nMasukkan Pilihan Anda: ")

                if choice == "1":
                    updateTuple()
                    readTable(tuplePelanggan, cusHeader)
                    main()

                elif choice == "2":
                    updateTuple()
                    readTable(tupleMobil, carHeader)
                    main()

                elif choice == "3":
                    updateTuple()
                    readTable(tupleSewa, rentHeader)
                    main()

                elif choice == "4":
                    readIndCus()
                    main()

                elif choice == "5":
                    readIndCar()
                    main()

                elif choice == "6":
                    main()
                
                else:
                    print("Input anda salah, silahkan coba lagi.")
        
        ## Sorted Choice
        elif choice == "3":
            displayDataChoice()
            choice = input("\nMasukkan pilihan anda: ")

            if choice == "1":
                updateTuple()
                print(sortedTable(dataPelanggan, 'Nama'))
                print("Diurutkan berdasarkan nama...")

            elif choice == "2":
                updateTuple()
                readTable(tupleMobil, carHeader)
                print("\nDiurutkan berdasarkan... \n1.Tahun \n2.Kategori \n3. Tipe")
                choice = input("\nMasukkan pilihan anda: ")
                if choice == "1":
                    print(sortedTable(dataMobil, 'Tahun Pembuatan'))
                    main()
                elif choice == "2":
                    print(sortedTable(dataMobil, 'Kategori'))
                    main()
                elif choice == "2":
                    print(sortedTable(dataMobil, 'Tipe Mobil'))
                    main()
            elif choice == "3":
                updateTuple()
                print(sortedTable(dataSewa, 'waktu_berakhir_sewa'))
                print("Diurutkan berdasarkan selesai sewa")
            elif choice == "4":
                main()

        ## Update Choice
        elif choice == "4":
            updateEntry()
            main()    

        ## Delete Choice
        elif choice == "5":
            deleteEntry()
            main()
        
        ## Exit Choice
        elif choice == "6":
            sys.exit()

        else:
            print("Input anda salah, silahkan coba lagi.")

# Cek, apakah script ini digunakan sebagai modul atau program utama
if __name__ == "__main__":
    main()
