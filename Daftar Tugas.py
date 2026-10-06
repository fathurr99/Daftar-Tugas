# Daftar untuk menyimpan tugas
daftar_tugas = []

while True:
    print("\n=== APLIKASI TO-DO LIST ===")
    print("1. Lihat Daftar Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print("\n--- DAFTAR TUGAS ---")
        if not daftar_tugas:
            print("Belum ada tugas tersimpan.")
        else:
            for nomor, tugas in enumerate(daftar_tugas, 1):
                print(f"{nomor}. {tugas}")

    elif pilihan == "2":
        tugas_baru = input("\nMasukkan tugas baru: ")
        if tugas_baru.strip() != "":
            daftar_tugas.append(tugas_baru)
            print(f"✓ '{tugas_baru}' berhasil ditambahkan!")
        else:
            print("Tugas tidak boleh kosong!")

    elif pilihan == "3":
        print("\n--- HAPUS TUGAS ---")
        if not daftar_tugas:
            print("Tidak ada tugas yang bisa dihapus.")
        else:
            for nomor, tugas in enumerate(daftar_tugas, 1):
                print(f"{nomor}. {tugas}")
            
            try:
                nomor_hapus = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
                if 1 <= nomor_hapus <= len(daftar_tugas):
                    tugas_terhapus = daftar_tugas.pop(nomor_hapus - 1)
                    print(f"✓ '{tugas_terhapus}' berhasil dihapus!")
                else:
                    print("Nomor tugas tidak ditemukan.")
            except ValueError:
                print("Masukkan angka nomor yang valid!")

    elif pilihan == "4":
        print("\nTerima kasih! Sampai jumpa lagi.")
        break

    else:
        print("Pilihan tidak valid, silakan pilih angka 1 - 4.")