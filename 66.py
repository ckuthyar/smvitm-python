import os
info1=os.getcwd()
print(info1)
colleges1=["Canara","SMVITM"]
colleges2=["4CN","4MW"]
for j in range(0,2,1):
    
    coll_name=colleges1[j]
    coll_code=colleges2[j]
    dir1=coll_name+"/"+coll_code
    os.mkdir(coll_name)
    lst1=[20,21,22,23]
    for i in range(0,4,1):
        os.mkdir(dir1+str(lst1[i]))
depts=["CS","EC","ME","CE"]
dir2="SMVITM/4MW"+str(lst1[0])+depts[0]
os.mkdir(dir2)
dir2="SMVITM/4MW"+str(lst1[0])+depts[1]
os.mkdir(dir2)
dir2="SMVITM/4MW"+str(lst1[0])+depts[2]
os.mkdir(dir2)
dir2="SMVITM/4MW"+str(lst1[0])+depts[3]
os.mkdir(dir2)
