def cetak_nilai_kuadrat(n):
    for i in range(n):
        print(i ** 2)

# Fungsi input() digunakan untuk meminta input dari pengguna
n = int(input("Masukkan nilai n: "))

# Memastikan bahwa nilai n berada dalam rentang yang valid
if 1 <= n <= 20:
    cetak_nilai_kuadrat(n)
else:
    print("Nilai n tidak valid. Harap masukkan nilai antara 1 dan 20.")
