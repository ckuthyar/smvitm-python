def calc1(n1,n2):
    num1=n1
    num2=n2

    sum1=num1+num2
    dif1=num1-num2
    prd1=num1*num2
    div1=num1/num2

    info=(str(sum1)+","+str(dif1)+","+str(prd1)+","+str(div1))
    return info

f1=open("in2.txt","r")
f2=open("out1.txt","w")

list1=f1.readline().replace("\n","").split(",")
n1=int(list1[0])
n2=int(list1[1])

result=calc1(9,6)
f2.write(result)
f2.close()
