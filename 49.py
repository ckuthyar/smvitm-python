import mod_rule2
lastchar="a"
print("Input word starting from",lastchar)
input1=input()
result=mod_rule2.rule2(lastchar, input1)
isdisqualified=result
if(isdisqualified):
    print("Player is disqualified")
else:
    print("Player has entered",input1)
    
