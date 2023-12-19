def diamond1(word1):
    s1=word1
    len1=len(s1)
    for i in range(0,len1+1,1):
        print("#"*(len1-i) + s1[0:i])
    for i in range(0,len1+1,1):
        print("#"*(i)+s1[0:len1-i])

diamond1("FUNWITHPROGRAMMING")
print()
