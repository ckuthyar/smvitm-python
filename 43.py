def rule4(s1,timeout):
    import datetime as dt
    timeout=timeout
    today1=dt.datetime.now()
    input1=input(s1+str(timeout)+": ")
    today2=dt.datetime.now()
    diff1=(today2-today1).seconds
    return(diff1,input1)


s1="Enter a word within seconds "
s2="Player is disqualified due to Rule4"
s3="Player has entered the word "
timeout=5
result=rule4(s1,timeout)
time1=result[0]
input1=result[1]
if(time1>timeout):
    print(s2)
else:
    print(s3,input1)

