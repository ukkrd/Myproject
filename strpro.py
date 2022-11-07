#1.Find all the possible combinations of char within the string. For example “123”---> “132” , “213”, “231” , “312” ……
a="123"
l=[]

for i in a:
    for j in a:
        if j != i:
            st=j+i
            l.append(st)
    for k in a:
        for p in range(len(l)):
            while k not in l[p]:
                l[p]=l[p]+k
            
for i in l:
    print(i)
    
     
        

