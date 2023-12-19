f1=open("words.txt","r")
list1=f1.read().split("\n")
len1=len(list1)
list2=[]
alpha=['a','b','c']

for i in range(0,len1,1):
    if(list1[i][0]=='b'):
        list2.append(list1[i])
    else:
        print()
print(list2)

 
