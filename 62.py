def confuse1(num1):
    
    cc1=num1
    len1=len(cc1)
    f1=open("city1.txt","a")
    f2=open("city2.txt","a")
    odd=""
    even=""
    for i in range(0,8,1):
        odd=odd+str(cc1[2*i])
    for i in range(0,8,1):
        even=even+cc1[1+2*i]
    f1.write(odd)
    f2.write(even)
    f1.write("\n")
    f2.write("\n")
    f1.close()
    f2.close()
    print(odd)
    print(even)
    print()
        
confuse1("9999888877776666")
confuse1("1234567890123456")


