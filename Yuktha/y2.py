def find_factorial():
    def fact(n):
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return fact(n-1)+fact(n-2)
    factorial =[]    
    for i in range(1,11,1):    
        factorial.append(fact(i))
    return factorial

print(find_factorial())
