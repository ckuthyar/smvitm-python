triad3 =[]
for i in range(1,20,1):
    for j in range(i+1,20,1):
        num1 = i**2
        num2 = j**2
        c =(num1+num2)**0.5 
        if c==int(c):
            triad3.append((i,j,int(c)))
print(triad3)   
