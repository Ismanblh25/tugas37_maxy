def masukan_angka():
    while True:
        try:
            angka = float(input("Masukkan angka: "))
            return angka
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka yang benar.")

def kalkulator():
    print("----- Kalkulator Sederhana -----")
    print("Pilih Menu:")
    print("0 – Masukkan angka")
    print("1 – Penjumlahan")
    print("2 – Pengurangan")
    print("3 – Perkalian")
    print("4 – Pembagian")
    print("5 – Keluar")

    angka1 = masukan_angka()
    
    while True:
        menu = input("\nPilih operasi (0-5): ")
        
        if menu == "0":
            angka1 = masukan_angka()

        elif menu in ["1", "2", "3", "4"]:
            angka2 = masukan_angka()
            
            if menu == "1":
                hasil = angka1 + angka2
                print(f"Hasil penjumlahan: {hasil}")
                
            elif menu == "2":
                hasil = angka1 - angka2
                print(f"Hasil pengurangan: {hasil}")
                
            elif menu == "3":
                hasil = angka1 * angka2
                print(f"Hasil perkalian: {hasil}")
                
            elif menu == "4":
                if angka2 != 0:
                    hasil = angka1 / angka2
                    print(f"Hasil pembagian: {hasil}")
                else:
                    print("Tidak dapat membagi dengan nol!")
                    
            angka1 = hasil  # Menggunakan hasil operasi sebagai angka pertama selanjutnya

        elif menu == "5":
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        else:
            print("Menu tidak valid. Silakan pilih antara 0-5.")

# Memanggil fungsi kalkulator
kalkulator()
