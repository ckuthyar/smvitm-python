f1=open("file1.txt","r")
f2=open("file2.txt","r")
list1=f1.readlines()
list2=f2.readlines()
list3=[]
list4=[]
difflines=[]
for i in range (0,4,1):
    line1=list1[i].replace("\n","")
    line2=list2[i].replace("\n","")
    if(line1!=line2):
        list3.append(line1)
        list4.append(line2)
        difflines.append(i)
lineno=difflines[0]
list5=list3[0].split(" ")
list6=list4[0].split(" ")
for i in range(0,2,1):
    
    word1=list5[i]
    word2=list6[i]
    if(word1!=word2):
        print("line",lineno,"word",i," mismatched",word1,word2)


