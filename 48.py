def rule2(lastchar,input1):
    isdisqualified=False
    lastchar=lastchar
    input1=input1
    len1=len(input1)
    firstchar=input1[0:1]
    if(firstchar!=lastchar):
        isdisqualified=True
    else:
        isdisqualified=False
    return(isdisqualified)

lastchar="a"
input1="apple"
result=rule2(lastchar, input1)
isdisqualified=result
if(isdisqualified):
    print("Player is disqualified")
else:
    print("Player has entered",input1)
    
    
