cc1="9876543210987654"
len1=len(cc1)
f1=open("city1.txt","w")
f2=open("city2.txt","w")
odd=""
even=""
for i in range(0,8,1):
    odd=odd+str(cc1[2*i])
for i in range(0,8,1):
    even=even+cc1[1+2*i]
f1.write(odd)
f2.write(even)
f1.close()
f2.close()
print(odd)
print(even)
        
