import mod_rule3

used=["apple","banana","carrot","drumstick","egg","fish"]
result=mod_rule3.rule3(used)
input1=result[1]
if(result[0]):
    print("Player disqualified")
else:
    print("Player has entered",input1)
