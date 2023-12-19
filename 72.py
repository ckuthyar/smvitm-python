days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
nums=[]
list2=[]

for i in range(0,365,1):
    nums.append(i+1)
    
for j in range(0,53,1):
    for i in range(0,7,1):
        list2.append(days[i])
print(list2)

