f1=open("in2.txt","r")
list1=f1.readline().split(",")
start=int(list1[0])
end=int(list1[1])
for j in range(start,end+1,1):
    
    for i in range(1,11,1):
        print(j,i,j*i)
    print()    
