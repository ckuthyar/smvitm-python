f1=open("in2.txt","r")
f2=open("out2.txt","w")
list1=f1.readline().split(",")
start=int(list1[0])
end=int(list1[1])
for j in range(start,end+1,1):
    
    for i in range(1,11,1):
        print(j,i,j*i)
        f2.write("pratham")
        f2.write("\n")
    print()    
f2.close()
