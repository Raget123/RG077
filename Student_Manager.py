# STUDENT GRADE MANAGER - FINAL VERSION
judul = "SISTEM MANAJERISASI SISWA"
print(f"{judul:^64}")

d_siswa = []

# --- FUNGSI TAMBAH ---
def tambah(nama, nilai):
    if not isinstance(nama, str) or nama == "":
        return "Nama harus diisi dengan benar!"
    if len(nilai) != 4:
        return "Harus ada 4 nilai (UTS1, UAS1, UTS2, UAS2)!"
    
    # Validasi semua isi nilai harus angka
    for n in nilai:
        if not isinstance(n, int):
            return "Semua nilai harus berupa angka bulat!"
        elif n < 0 or n > 100:
            return "Nilai Gak Masuk Akal!"
            
    d_siswa.append({"NAMA": nama, "NILAI": nilai})
    return f"Data {nama} berhasil ditambah!"

# --- FUNGSI HAPUS ---
def hapus(nama):
    if len(d_siswa) == 0:
        return "Data masih kosong!"
    for siswa in d_siswa:
        if siswa["NAMA"].upper() == nama.upper():
            d_siswa.remove(siswa)
            return f"Data {nama} berhasil dihapus!"
    return "Nama tidak ditemukan!"

# --- FUNGSI LIHAT ---
def lihat():
    if not d_siswa:
        print("\n[!] Data Kosong!")
        return
    
    print(f"\n{'DATA SISWA':^64}")
    print("-" * 64)
    for s in d_siswa:
        n = s["NILAI"]
        print(f"Nama  : {s['NAMA']}")
        print(f"Nilai : UTS1:{n[0]} | UAS1:{n[1]} | UTS2:{n[2]} | UAS2:{n[3]}")
        print("-" * 30)

# --- FUNGSI EDIT ---
def edit(nama, exam, baru):
    exm_list = ["UTS 1", "UAS 1", "UTS 2", "UAS 2"]
    for s in d_siswa:
        if s["NAMA"].upper() == nama.upper():
            if exam.upper() in exm_list:
                idx = exm_list.index(exam.upper())
                if baru < 0 or baru > 100:
                    return "Nilai Gak Masuk Akal!"
                else:
                    s["NILAI"][idx] = baru
                    return f"Nilai {exam.upper()} {nama} diubah jadi {baru}!"
            return "Jenis ujian salah! (Contoh: UTS 1)"
    return "Nama tidak ada di data!"

# --- FUNGSI ANALISIS (UPGRADED) ---
def analisis(target, jenis):
    if not d_siswa: return "Data kosong!"
    
    # Penentuan Target
    if target.upper() == "SEMUA":
        data = d_siswa
    else:
        found = [s for s in d_siswa if s["NAMA"].upper() == target.upper()]
        if not found: return "Nama tidak ditemukan!"
        data = found

    # 1. RATA-RATA & MIN/MAX
    if jenis.upper() == "RATA-RATA":
        for s in data:
            rata = sum(s["NILAI"]) / 4
            print(f"\n> {s['NAMA']}")
            print(f"  Rata-rata: {rata}")
            print(f"  Tertinggi: {max(s['NILAI'])} | Terendah: {min(s['NILAI'])}")

    # 2. DIFERENSI (Progres Awal ke Akhir)
    elif jenis.upper() == "DIFERENSI":
        for s in data:
            dif = s["NILAI"][3] - s["NILAI"][0]
            print(f"> {s['NAMA']} | Selisih UAS 2 - UTS 1: {dif}")

    # 3. RANKING (Hanya Semua)
    elif jenis.upper() == "RANKING":
        rank = sorted(d_siswa, key=lambda x: sum(x["NILAI"]), reverse=True)
        print("\n=== PERINGKAT SISWA ===")
        for i, s in enumerate(rank, 1):
            print(f"{i}. {s['NAMA']} (Total: {sum(s['NILAI'])})")

    # 4. FILTER LULUS (KKM 75)
    elif jenis.upper() == "FILTER":
        print("\n=== STATUS KELULUSAN (KKM 75) ===")
        for s in data:
            rata = sum(s["NILAI"]) / 4
            status = "LULUS" if rata >= 75 else "REMEDI"
            print(f"- {s['NAMA']}: {status} ({rata})")

# --- MENU UTAMA (WHILE LOOP) ---
while True:
    print("\n[ MENU UTAMA ]")
    print("1. Lihat | 2. Tambah | 3. Hapus | 4. Edit | 5. Analisis | 6. Keluar")
    pilih = input("Pilih Opsi: ")

    if pilih == "1":
        lihat()
    
    elif pilih == "2":
        nm = input("Nama Siswa: ")
        try:
            gl = [int(input(f"Nilai ke-{i+1}: ")) for i in range(4)]
            print(tambah(nm, gl))
        except ValueError: print("Input harus angka!")

    elif pilih == "3":
        print(hapus(input("Nama yang dihapus: ")))

    elif pilih == "4":
        nm = input("Nama Siswa: ")
        uj = input("Ujian (UTS 1/UAS 1/UTS 2/UAS 2): ")
        try:
            nb = int(input("Nilai Baru: "))
            print(edit(nm, uj, nb))
        except ValueError: print("Nilai harus angka!")

    elif pilih == "5":
        tr = input("Target (Semua / Nama Siswa): ")
        jn = input("Jenis (Rata-Rata / Diferensi / Ranking / Filter): ")
        err = analisis(tr, jn)
        if err: print(err)

    elif pilih == "6":
        print("Program Selesai. Selamat Istirahat!")
        break
