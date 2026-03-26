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
            