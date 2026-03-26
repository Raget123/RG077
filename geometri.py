def triangle(n,s):
    if not isinstance(n,int):
        raise ValueError("n Integer Please")
    else:
        rs = str(s)
        for i in range(1,n):
            row = f"{rs} " * i
            print(f"\t{row :^{4*n}}")
            
triangle(9,"=")

def rectangle(n,s):
          if not isinstance(n,int):
               raise ValueError("n Integer Please")
          else:
               rs = str(s)
               for _ in range(1,n+1):
                  row = f"{rs} " * (2*n-1)
                  print(f"\t{row:^{4*n}}")
             
rectangle(4," = ")

def diamond(n,s):
    if not isinstance(n,int):
           raise ValueError("n Integer Please")
    else:
            w = 2*n-1
            m = 1
            for m in range(1,w+1,2):
                print(f"{s * m:^{w}}")
            for m in range(w-2,0,-2):
                print(f"{s *m:^{w}}")
                
            
diamond(8,"*")


