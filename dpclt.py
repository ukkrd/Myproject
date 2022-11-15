'''2.  In an array 1-100 multiple numbers are duplicates,
Find all the duplicate numbers'''

def dplct(a=[]):
    dpt=[]
    a.sort()
    temp=0
    for i in a:
        if temp==i:
            dpt.append(i)
        else:
            temp=i
        
       
    print("deplicate number in array:")
    for s in dpt:
        print(s)
# here you can pass any array in dplct function as a argument            
dplct([i for i in range(1,101)])

