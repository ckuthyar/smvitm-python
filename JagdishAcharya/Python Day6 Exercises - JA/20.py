def topper1(fname, gold_medalist,maxallsubj,schoolname):
    list1=fname.split(".")
    school_name=list1[0]
    
    with open(fname,'r') as file:
        lines1 = file.readlines()
        numoflines = len(lines1)
        print("School Name:",school_name," and Number of Students:",numoflines)

    f1=open(fname,"r")
        
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

    for i in range(0,numoflines,1):    
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

    #print(names)
    #print(subjects[0],sub1)
    #print(subjects[1],sub2)
    #print(subjects[2],sub3)
    #print(subjects[3],sub4)
    #print(subjects[4],sub5)

    #print("Total",allsubj)
        
    max_sub1=max(sub1)
    max_sub2=max(sub2)
    max_sub3=max(sub3)
    max_sub4=max(sub4)
    max_sub5=max(sub5)
    max_all_subj=max(allsubj)

    for i in range(0,numoflines,1):
        if sub1[i]==max_sub1:
            toppers_sub1.append(names[i])
        if sub2[i]==max_sub2:
            toppers_sub2.append(names[i])
        if sub3[i]==max_sub3:
            toppers_sub3.append(names[i])
        if sub4[i]==max_sub4:
            toppers_sub4.append(names[i])
        if sub5[i]==max_sub5:
            toppers_sub5.append(names[i])
        if allsubj[i]==max_all_subj:
            gold_medalist.append(names[i])

    f1.close()
    
    print(toppers_sub1, " - toppers with marks in",subjects[0], max_sub1)
    print(toppers_sub2, " - toppers with marks in",subjects[1], max_sub2)
    print(toppers_sub3, " - toppers with marks in",subjects[2], max_sub3)
    print(toppers_sub4, " - toppers with marks in",subjects[3], max_sub4)
    print(toppers_sub5, " - toppers with marks in",subjects[4], max_sub5)

    print("Gold Medalist in ",school_name, "with highest marks", max_all_subj, gold_medalist)
    print()

    return(gold_medalist, max_all_subj, school_name)


##### Main #####
#fname=input("Enter File Name w/o .txt: ")
#fname=fname+".txt"
fname="GoldMedalFiles.txt"

with open(fname,'r') as file:
   lines1 = file.readlines()
numoflines = len(lines1)
print("Number of Schools:",numoflines)
print()

f1=open(fname, "r")

gold_medalist1=""
total_marks1=0
schoolname1=""
gold_medalist_all=[]
total_marks_all=[]
schoolname_all=[]
topper_all_schools=[]
schools_all=[]

for i in range(0,numoflines,1):    
    fname1=f1.readline().replace("\n","")
    list1=fname1.split(".")
    schoolname=list1[0]
    
    list2 = topper1(fname1,gold_medalist1,total_marks1,schoolname1)
    
    gold_medalist_all.append(list2[0])
    total_marks_all.append(list2[1])
    schoolname_all.append(list2[2])
    
    #print(gold_medalist_all)

maxtotalallschools=max(total_marks_all)
#print(total_marks_all)

for i in range(0,numoflines,1):
    if total_marks_all[i]==maxtotalallschools:
        topper_all_schools.append(gold_medalist_all[i])
        schools_all.append(schoolname_all[i])

f1.close()

print("Overall Topper in ALL Schools with highest marks",maxtotalallschools)
for i in range(len(topper_all_schools)):
    print(topper_all_schools[i], "in",schools_all[i])
    
print()




    
