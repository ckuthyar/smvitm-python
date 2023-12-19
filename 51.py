import mod_rule1
words=[["apple","art"],["box","baby"],["cat","carrot"],["drum","day"]]
input1="art"
result=mod_rule1.rule1(words,input1)
isdisqualified=result
if(isdisqualified):
    print("Player is disqualfied")
else:
    print("Game can proceed")
    
