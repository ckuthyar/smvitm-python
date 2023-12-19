def rule1(words,input1):
    words=words
    input1=input1
    alpha=['a','b','c','d']
    firstletter=input1[0:1]
    position=alpha.index(firstletter)
    isdisqualified=False
    if(input1 in words[position]):
        isdisqualified=False
    else:
        isdisqualified=True
    return(isdisqualified)

words=[["apple","art"],["box","baby"],["cat","carrot"],["drum","day"]]
input1="camel"
result=rule1(words,input1)
isdisqualified=result
if(isdisqualified):
    print("Player is disqualfied")
else:
    print("Game can proceed")
    
