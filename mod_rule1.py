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
    return(isdisqualified,position)


