def Greeating(nama):
    print("halo", nama)

Greeating("Yanto")

#fungsi dengan mengembalikan nilai
def penjumlahan(a, b):
    hasil = a + b
    return hasil

Greeating("Samsudin")

hasil_penjumlahan = penjumlahan(7, 9)
print("Hasil Penjumlahan adalah", hasil_penjumlahan)
print(f"Hasil Penjumlahan adalah {hasil_penjumlahan}")

#fungsi dengan variable panjang argument(*args)
def jumlahkan(*args):
    total = 0
    for angka in args:
        total += angka
    return total

hasil = jumlahkan(10, 20, 30, 40, 50)
print(f"Hasil Penjumlahan: {hasil}")        