#=====GAME QUIZ MTK=====
nama = input("Masukkan Nama Anda : ")
umur = int(input("Masukkan Umur Anda : "))
main = input("Mau Bermain? (Tulis apapun Untuk main,selain N) : ")
if main.upper() == "N":
    exit()

soal = {
"soal_1":
    ["Jika x + 7 = 12, Maka x = ?...\n",5],
    
"soal_2":
    ["\nBerapa banyak faktor positif dari 2^5 + 3^5 ?\n", 6],
    
"soal_3":
    ["\nSebuah Sudut ABD bertolak belakang dengan sudut CBE. Jika Sudut CBA adalah 62°. Maka berapakah Sudut ABD?\n",118],
    
"soal_4":
    ["\nA = {2,3,7,8,10,15,63} , B = {x | x € Z+, x² - 1, x <= 8}. maka n(A u B) adalah? (gabungan)\n",11],
    
"soal_5":
    ["\nBerapakah Digit terakhir dari 2^7 + 8^13?\n",6]
}
    

score = 0
for s in soal.values():
    tm = int(input(s[0]))
    if tm != s[1]:
        print("Salah!")
        score -= 3
    else:
        print("Benar!")
        score += 5
        
print(f""" 
Selamat! Soal Terselesaikan 5/5.
nama : {nama}
umur : {umur}

Score : {4*score}
""")
    