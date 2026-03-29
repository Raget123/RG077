#Market Inventory

inventory = []

#Menambah Produk
def tambah(produk,harga):
    if not isinstance(produk,str) or not isinstance(harga,int):
        return "Masukkan Produk dan Harga Yang bener woi!"
    else:
         if harga < 0:
             return "Masukkan Harga Yang Bener Dong!"
         else:
              for p in inventory:
                  if p["P"] == produk.lower():
                      return "Produk Itu Sudah Ada!"
                      
              inventory.append({"P":produk.lower() , "H":harga,"S":0})
              return f"Produk {produk} Sudah Berhasil dimasukkan!"

#Restock Produk          
def restock(produk,banyak):
         if not isinstance(produk,str) or not isinstance(banyak,int):
             return "Masukkan Produk dan Banyaknya Yang bener woi!"
         else:
             if banyak < 0:
                 return "Masukkan Angka Yang Bener Dong!"
             else:
                  for p in inventory:
                      if p["P"] == produk.lower():
                          p["S"] += banyak
                          return "Stock Produk berhasil ditambah"
                  return "Gak Ada Tuh Produk Nya"
                          
#Menjual Produk
def jual(produk,jual):
         if not isinstance(produk,str) or not isinstance(jual,int):
             return "Masukkan Produk dan Banyaknya Yang bener woi!"
         else:
             if jual < 0:
                 return "Masukkan Angka Yang Bener Dong!"
             else:
                  for p in inventory:
                      if p["P"] == produk.lower():
                          if p["S"] <= 0:
                              return "Gakada Produk Yang Bisa dijual!"
                          elif  p["S"] < jual:
                               return "Stok Kurang Untuk dijual!"
                          else:
                                p["S"] -= jual
                                return "Produk berhasil dijual!"
                  return "Gak Ada Tuh Produk Nya"     '' 
#Edit Harga
def edit(produk,harga):
    if not isinstance(produk,str) or not isinstance(harga,int):
        return "Masukkan Produk dan Harga Yang bener woi!"
    else:
         if harga < 0:
             return "Masukkan Harga Yang Bener Dong!"
         else:
              for p in inventory:
                  if p["P"] == produk.lower():
                      p["H"] = harga
                      return "Harga Berhasil diubah!"
              return "Gakada Produk Buat Diubah Harga!"
    
#Lihat Produk
def lihat():
         if len(inventory) == 0:
             print("Gakada Produk Nya! Masukkin Dulu Boss!!...")
             
         print("====Produk–Produk=====\n")
         for p in inventory:
             total = p["H"]*p["S"]
             print(f"Produk : {p['P']}\n Harga : Rp. {p['H']:,}\n Stok : {p['S']} Buah \n -------------")
             
         print(f"Total Aset : Rp{total}")
         
header = "Inventory Raget Market"
print(f"{header:^64}")

while True:
             try:
                 menu = int(input(f"Manager Menu :\n 1. Masukkan Produk\n 2. Restock Barang\n 3. Jual \n 4. Edit Harga\n 5. Lihat Produk\n 6. Keluar\n (Masukkan Angka nya aja!)\n"))
                 if menu == 1:
                     produk = input("Masukkan Nama Produk : ")
                     harga = int(input("Masukkan Harga Produk : "))
                     status = tambah(produk,harga)
                     print(status)
                 elif menu == 2:
                     produk = input("Pilih Produk Yang Mau Ditambah : ")
                     stok = int(input("Berapa Banyak Restoknya? : "))
                     status = restock(produk,stok)
                     print(status)
                 elif menu == 3:
                     produk = input("Pilih Produk Yang Terjual : ")
                     banyak = int(input("Seberapa Banyak? : "))
                     status = jual(produk,banyak)
                     print(status)
                 elif menu == 4:
                    produk = input("Produk Mana Yang Mau di Edit? : ")
                    ubah = int(input("Ubah Ke Harga Berapa? : "))
                    status = edit(produk,ubah)
                    print(status)
                 elif menu == 5:
                    lihat()
                 elif menu == 6:
                    print("Program Dihentikan...")
                    break
                 else:
                    print("Gakada Menu Itu!!")
             except ValueError:
                    print("Dibilang Angka aja!!")