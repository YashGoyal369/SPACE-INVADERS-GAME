import ast
with open("h.txt","r") as f:
        ply=str(input("Player Name:"))
        a=f.read()
        l=[]
        b=ast.literal_eval(a)
        c=str(b.keys())
        for i in b:
               if ply==i :
                      d=b[i]
                      print(d)
               else:
                     print(c)
        for i in b:
              l.append(b[i])
              print(l)
