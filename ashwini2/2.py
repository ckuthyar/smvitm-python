s1="ASHWINI IS LEARNING PROGRAMMING"
s2=""
len1=len(s1)
print(len1)
for i in range(0,len1,1):
    s2=s2+(s1[len1-(i+1):len1-i])
print(s2)


