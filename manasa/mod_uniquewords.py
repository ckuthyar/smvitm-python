def uniquewords(word1):
    s1=word1
    list1=s1.split(" ")
    set1=set(list1)
    list2=list(set1)
    list2.sort()
    print(list2)
