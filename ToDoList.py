#To-Do List

tugas = []

header = "To Do List"
print(f"{header:=^64}")
      
#Menambah Tugas
def task(tgs,prt):
    if not isinstance(tgs,str) or not isinstance(prt,int):
        return "Masukkan Tidak sesuai Aturan"
    for t in tugas:
        if t["T"] == tgs:
             return "Tugas Itu Sudah Ada"
             
    tugas.append({"T":tgs.lower(), "P":prt,"S":"PENDING"})
    return "Tugas Berhasil ditambakan!"

#Menyelesaikan Tugas        
def selesai(tgs):
    if not isinstance(tgs,str):
        return "Masukkan Tidak sesuai Aturan"
    else:
        jc1,jc2 = "yes","ngak"
        for t in tugas:
            if t["T"] == tgs.lower():
                cn = input("Beneran Sudah selesai? (y/yes, n\\gak) : ").lower()
                if cn in jc1:
                    t["S"] = "DONE"
                    return "Tugas Sudah diselesaikan!"
                elif cn  in jc2:
                    t["S"] = "PENDING"
                    return "Katanya sudah selesai!!"
        return "Gakada Tugas Itu Pe A!"
        
#Menghapus Tugas
def hapus(tgs):
    if not isinstance(tgs,str):
        return "Masukkan Tidak Sesuai Aturan"
    else:
         global tugas
         for t in tugas:
             if t["T"] == tgs.lower():
                 tugas.remove(t)
                 return "Tugas Berhasil dihapus"
         return "Gakada Tugas Untuk Dihapus!"

#Edit          
def edit(tgs,tgs_baru):
    if not isinstance(tgs,str) or not isinstance(tgs_baru,str):
          return "Masukkan Tidak Sesuai Aturan"
    else:
          for t in tugas:
              if t["T"] == tgs:
                  t["T"] = tgs_baru
                  return "Tugas Berhasil Di Edit!"
          return "Gak Ada Tugas Yang Mau Di Edit!"

#Sorting 
def sorting(j):
        if not isinstance(j,int):
            return None
        else:
            if j == 1: #1 = Sort Berdasarkan Prioritas
                return sorted(tugas, key=lambda t : t["P"])
            elif j == 2: #2 = Sort Berdasarkan Abjad
                return sorted(tugas, key=lambda t : t["T"])
        return tugas

#Lihat          
def lihat():
    try:
        ty = int(input("Mau Lihat Dari Bentuk apa? :\n 1. Prioritas\n 2. Abjad\n"))
        if ty == 1:
            for st in sorting(1):
                h = "High" if st["P"] == 1 else ("Medium" if st["P"] == 2 else "Low")
                print(f"{st['P']}. {st['T']} | Priority : {h} | Status : {st['S']}")
        elif ty == 2:
            for st in sorting(2):
                print(f"{st['P']}. {st['T']}")
        else:
             for st in tugas:
                h = "High" if st["P"] == 1 else ("Medium" if st["P"] == 2 else "Low")
                print(f"{st['P']}. {st['T']} | Priority : {h} | Status : {st['S']}")
    except ValueError:
          print("Masukkin Yang Bener Elah!")
          
#—Menu—


while True:
  print("\n1. Masukkan Tugas\n2. Selesaikan Tugas\n3. Edit Tugas\n4. Hapus Tugas\n5. Keluar")
  
  try:
      menu = int(input("Pilih Pengolahan Tugas : "))
      
      if menu == 1:
          masuk = input("Masukkan Tugas : ")
          prio = int(input("Masukkan Angka Prioritas :\n 1. High\n 2. Medium\n 3. Low\n"))
          status = task(masuk,prio)
          print(status)
        
          see = input("Mau Lihat Daftar Tugas? (y/n) : ").lower()
          if see == "y":
            lihat()
          continue
      elif menu == 2:
           complete = input("Tugas Mana Sudah selesai? : ")
           status = selesai(complete)
           print(status)
           
           see = input("Mau Lihat Daftar Tugas? (y/n) : ").lower()
           if see == "y":
                  lihat()
           else:
                  print("Oke!")
      elif menu == 3:
            awal = input("Masukkan Tugas Yang mau di edit! : ")
            akhir = input("Masukkan Tugas Baru : ")
            status = edit(awal,akhir)
            print(status)
            
            see = input("Mau Lihat Daftar Tugas? (y/n) : ").lower()
            if see == "y":
                  lihat()
            else:
                  print("Oke!")
      elif menu == 4:
            dlt = input("Masukkan Tugas Yang mau di Hapus! : ")
            status = hapus(dlt)
            print(status)
            
            see = input("Mau Lihat Daftar Tugas? (y/n) : ").lower()
            if see == "y":
                  lihat()
            else:
                  print("Oke!")
      elif menu == 5:
          print("Oke Kalau Gitu!")
          break
      else:
          print("Lu Pilih Apaan Peak!\n")
          
  except ValueError: 
      print("Harus Milih 1-5 Ya boss. Pakai nya Angka!!")
      
print("Raget - Program selesai")