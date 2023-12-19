def factn(num1):
    if num1==1:
        return 1
    else:
        return num1*factn(num1-1)
