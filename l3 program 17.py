t=int(input("enter instance time:"))
e=[7,0,5,1,3]
l=[1,2,1,3,4]
x=[0,0,0,0,0] 
for i in range(t):
    if t>len(e) or t>len(l):
        print("out of index")
    else:
        x[i]=(x[i-1]+e[i])-l[i] 
        print(x[i],end=" ")
print("\nmax:",max(x))

