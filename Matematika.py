#Modul Matematika

#Akar
def roots(a,m,n):
      akar = a**(m/n)
      return akar
      
#Persen
def percent(n):
      persen = n/100
      return f"{persen:.1%}"

#Permil      
def permils(n):
      permil = n/1000
      return f"{permil}"

#Rata Rata    
def avg(*data):
      dlist = list(data)
      return sum(dlist)/len(dlist)

#Median      
def med(*data):
      dlist = list(data)
      dlist.sort()
      n = len(dlist)
      if n % 2 == 1:
            ganjil = (n-1)//2
            med = dlist[ganjil]
      elif n % 2 == 0:
            genap_1 = dlist[(n//2) - 1]
            genap_2 = dlist[n//2]
            med = (genap_1+genap_2)/2
      return med
      

#Faktorial      
def factorial(limit):
      a = 1
      for i in range(1,limit+1):
            a *= i
      return a

#Invers 
def inv(angka):
      invers = angka - (angka * 2)
      return invers
      
#Range Data 
def rgdata(*data):
      dlist = list(data)
      dlist.sort()
      rdata = max(dlist) - min(dlist)
      return rdata
      
#Membentuk Pecahan
def pch(m:int,n:int) -> int:
      return f"{m}/{n}"
      
#Membentuk Pecahan Campuran
def cmp(a,b):
      sisa = a % b
      hasil = a // b
      bentuk = f"{hasil} {sisa}/{b}"
      return bentuk
      



