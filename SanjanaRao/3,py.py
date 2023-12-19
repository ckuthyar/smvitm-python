def table1(start,end):   
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()
f1=open("table1.txt","r")
start=int(f1.readline())
end=int(f1.readline())
table1(start,end)
