def rev1(word1):
    
    s1=word1
    s2=""
    len1=len(s1)
    for i in range(0,len1,1):
        s2=s2+(s1[len1-(i+1):len1-i])
    print(s2)

rev1("SHREYA TANTRY")
rev1("SANJANA RAO")
rev1("ASHWINI")

