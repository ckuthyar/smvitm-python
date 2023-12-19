def rule3(list1,s1,s2,s3):
    isdisqualified=False
    used=list1
    print(s1)
    input1=input()
    if input1 in used:
        isdisqualifed=True
    else:
        isdisqualifed=False
    return(isdisqualifed,input1)

s1="Enter a word which is not used before by either player or computer"
s2="Player is disqualified due to Rule3"
s3="Player has entered the word "
used=["apple", "banana", "cat", "dog", "elephant", "fish", "goat", "horse"]
result=rule3(used,s1,s2,s3)
if(isdisqualifed):
    print(s2)
else:
    

print(result[0])
print(result[1])
