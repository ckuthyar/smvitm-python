def table1(start,end):   
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()
table1(3,20)
table1(50,55)
table1(2000,2003)
