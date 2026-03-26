#The Sum of Modulus

def μ(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise ValueError("Input The Integer Number In Parameter!")
    else:
        if a**2 > b:
            return f"Only a² < b, Your Input → {a**2} > {b}"
        else:
            if a < 0:
                return "Only Positif"
            else:
                ls = 0
                for n in range(1,a+1):
                    ls += b % n
                    
               
                return ls
"""lnum = []
for i in range(1,100):
      x = μ(i,(100**2 + 1))
      lnum.append(x)
      
print(lnum)"""

p = []
for k in range(1,20):
    t =  μ(1250,1250**2+k)
    p.append(t)
    
print(p)
print(μ(1250, 1562519) == μ(1249, 1562519))