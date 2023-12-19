f1=open("GoldMedal.txt", "r")
subjects=[]
names=[]
sub1=[]
toppers_sub1=[]
sub2=[]
toppers_sub2=[]
sub3=[]
toppers_sub3=[]
sub4=[]
toppers_sub4=[]
sub5=[]
toppers_sub5=[]
allsubj=[]
gold_medalist=[]

for i in range(0,26,1):    
    info1=f1.readline()
    list1=info1.split(",")
    if i==0:
        list1a=list1[3].split(":")
        subjects.append(list1a[0])
        list1a=list1[4].split(":")
        subjects.append(list1a[0])
        list1a=list1[5].split(":")
        subjects.append(list1a[0])
        list1a=list1[6].split(":")
        subjects.append(list1a[0])
        list1a=list1[7].split(":")
        subjects.append(list1a[0])        
    names.append(list1[0])
    list2=list1[3].split(":")
    sub1.append(int(list2[1]))
    list2=list1[4].split(":")
    sub2.append(int(list2[1]))
    list2=list1[5].split(":")
    sub3.append(int(list2[1]))
    list2=list1[6].split(":")
    sub4.append(int(list2[1]))
    list2=list1[7].split(":")
    sub5.append(int(list2[1]))
    allsubj.append(sub1[i]+sub2[i]+sub3[i]+sub4[i]+sub5[i])

print(names)
print(subjects[0],sub1)
print(subjects[1],sub2)
print(subjects[2],sub3)
print(subjects[3],sub4)
print(subjects[4],sub5)

print("Total",allsubj)
    
maxsub1=max(sub1)
maxsub2=max(sub2)
maxsub3=max(sub3)
maxsub4=max(sub4)
maxsub5=max(sub5)
maxallsubj=max(allsubj)

for i in range(0,26,1):
    if sub1[i]==maxsub1:
        toppers_sub1.append(names[i])
    if sub2[i]==maxsub2:
        toppers_sub2.append(names[i])
    if sub3[i]==maxsub3:
        toppers_sub3.append(names[i])
    if sub4[i]==maxsub4:
        toppers_sub4.append(names[i])
    if sub5[i]==maxsub5:
        toppers_sub5.append(names[i])
    if allsubj[i]==maxallsubj:
        gold_medalist.append(names[i])

print(toppers_sub1, " - toppers with marks in",subjects[0], maxsub1)
print(toppers_sub2, " - toppers with marks in",subjects[1], maxsub2)
print(toppers_sub3, " - toppers with marks in",subjects[2], maxsub3)
print(toppers_sub4, " - toppers with marks in",subjects[3], maxsub4)
print(toppers_sub5, " - toppers with marks in",subjects[4], maxsub5)

print(gold_medalist, "- Gold Medalist with highest marks", maxallsubj)



    
