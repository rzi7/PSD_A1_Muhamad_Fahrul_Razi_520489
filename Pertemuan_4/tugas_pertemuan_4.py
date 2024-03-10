# Fungsi untuk menghitung nilai rata rata
def rata(data):
    total = 0
    for i in range(len(data)):
        total += data[i]

    rata = total / len(data)
    return rata

# Fungsi untuk memasukkan data mahasiswa ke dalam array 
def mahasewa(n):
    dataMahasewa = []

    for i in range(n):
        data = []
        nilai = []
        a = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
        b = input(f"Masukkan NIM mahasiswa ke-{i+1}: ")
        print()
        data.append(a)
        data.append(b)

        banyakNilai = int(input(f"Masukkan jumlah nilai ujian mahasiswa ke-{i+1}: "))
        for j in range(banyakNilai):
            scor = float(input(f"Masukkan nilai ujian ke-{j+1}: "))
            nilai.append(scor)
        nilai = rata(nilai)
        data.append(nilai)
        print()
        dataMahasewa.append(data)

    return dataMahasewa

banyak = int(input("Masukkan jumlah mahasiswa: "))
dataMahasiswa = mahasewa(banyak)

for i in range(len(dataMahasiswa)):
    print(f"Nama: {dataMahasiswa[i][0]}")
    print(f"NIM: {dataMahasiswa[i][1]}")
    print(f"Rata-rata Nilai Ujian: {dataMahasiswa[i][2]}")
    print()
    if i < (len(dataMahasiswa)-1):
        print("==================================================")
    print()

