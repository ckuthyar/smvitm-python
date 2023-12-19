def factn(num1):
    if num1==1:
        return 1
    else:
        return num1*factn(num1-1)

print(factn(2))
print(factn(3))
print(factn(4))
