def rule4(timeout):
    import datetime as dt
    timeout=timeout
    today1=dt.datetime.now()
    input1=input()
    today2 = dt.datetime.now()
    differ1=(today2-today1).seconds
    return (differ1,input1)