word3="EAT"
def perm3(word3):
    word3=word3
    list3=[]
    s1=word3[0:1]
    s2=word3[1:2]
    s3=word3[2:3]
    list3.append(s1+s2+s3)
    list3.append(s1+s3+s2)
    list3.append(s2+s1+s3)
    list3.append(s2+s3+s1)
    list3.append(s3+s1+s2)
    list3.append(s3+s2+s1)
    print(list3)
#perm3("EAT")
#perm3("TRY")
#perm3("ASK")


word4="FAST"
part1="F"
part2="AST"
perm3(part2)
