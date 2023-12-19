list1=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for j in range(0,10,1):
    
    p1=list1[j]*list1[j]
    for i in range(0,10,1):
        p2=list2[i]*list2[i]
        p3=(p1+p2)**0.5
        p33=int(p3)
        diff1=p3-p33
        if diff1==0:
            print(list1[j],list2[i],p33,"is a triad") 







