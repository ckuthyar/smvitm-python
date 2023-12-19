figwords={1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
print(figwords.keys())
print(figwords.values())
print(figwords.items())

figwords2=figwords.copy()
print(figwords2.keys())

figwords2.clear()
print(figwords2.keys())


even1=[2,4,6,8,8]
even2=set(even1)
even3=list(even2)
even3.sort()
print(even2)
print(even3)
