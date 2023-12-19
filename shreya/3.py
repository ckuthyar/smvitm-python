def cal1():
    print("mon","tue","wed","thu","fri","sat","sun")
    for j in range(0,31,7):
        for i in range(j,j+7,1):
            print((i%31)+1,end=" ")
        print()

def cal2():
    print("$","$","$",end=" ")
    for i in range(0,4,1):
        print((i%29)+1,end=" ")
    print()
    for j in range(4,29,7):
        for i in range(j,j+7,1):
            print((i%29)+1,end=" ")
        print()
    print()
cal1()
print()
cal2()
