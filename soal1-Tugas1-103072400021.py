def is_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False

tahun_input = int(input("Masukkan tahun: "))
hasil = is_kabisat(tahun_input)

print("Apakah tahun kabisat?", hasil)
