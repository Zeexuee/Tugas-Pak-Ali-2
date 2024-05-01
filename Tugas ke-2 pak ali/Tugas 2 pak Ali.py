def cetak_kuadrat_ganjil(n):
    for i in range(n):
        if i % 2 != 0:  
            print(i ** 2)


n = int(input("Masukkan nilai n: "))


if n >= 0:
    cetak_kuadrat_ganjil(n)
else:
    print("Nilai n tidak valid. Harap masukkan nilai non-negatif.")
