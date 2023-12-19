def table1(start,end):   
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
table1(num1,num2)
