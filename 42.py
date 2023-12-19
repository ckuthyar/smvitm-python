import datetime as dt
timeout=10
today1=dt.datetime.now()
input1=input("Enter a word within "+str(timeout)+" seconds: ")
today2=dt.datetime.now()
diff1=(today2-today1).seconds
if(diff1>timeout):
    print("Player is disqualified due to Rule4")


