import mod_rule4 as mr4

s1="Enter a word within seconds "
s2="Player is disqualified due to Rule4"
s3="Player has entered the word "
timeout=5
result=mr4.rule4(s1,timeout)
time1=result[0]
input1=result[1]
if(time1>timeout):
    print(s2)
else:
    print(s3,input1)

