def calc1(n1,n2):
    
    num1=n1
    num2=n2
    sum1=num1+num2
    dif1=num1-num2
    mul1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    result=str(sum1)+","+str(dif1)+","+str(mul1)+","+str(div1)+","+str(div2)+","+str(rem1)+","+str(exp1)
    print(result)
f1=open("in2.txt","r")
list1=f1.readline().split(",")
n1=int(list1[0])
n2=int(list1[1])
calc1(n1,n2)
