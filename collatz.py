#Collatz Conjecture
import statistics as st

def collatz(x):
    if not isinstance(x,int):
        return "Integer Number Only"
    else:
        h = []
        while x > 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3*x + 1
            h.append(x)
        return h
            



def HC(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        return "Integer Number Only"
    else:
         if a < 0 or b < 0:
             return "Only Positive Number"
         else:
             hn = set()
             ls = []
             for n in range(a,b+1):
                 s = collatz(n)
                 hn.update(s)
                 ls.append(s)
             ln = list(hn)
             p = (2/st.median(ln)) * (sum(ln)/len(ln))
             return p
            
print(HC(121))