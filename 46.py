def rule3(list1):
    used=list1
    len1=len(used)
    input1=input("Enter a word: ")
    isdisqualified=False
    if input1 in used:
        isdisqualified=True 
    else:
        print()
    return(isdisqualified,input1)

        
used=["apple","banana","carrot","drumstick","egg","fish"]
result=rule3(used)
input1=result[1]
if(result[0]):
    print("Player disqualified")
else:
    print("Player has entered",input1)



