
s1="today is a fine day. we are all going for a picnic. yesterday it rained heavily. so we thought that the picnic will be cancelled"

list1=s1.split(" ")
set1=set(list1)
list2=list(set1)
list2.sort()

print(list2)
