def figword1(num1):
    list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
    list2=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    input1=num1
    position1=list1.index(input1)
    output1=list2[position1]
    print(output1, end=" ")

num1=21
temp1=(num1//10)*10
part2=num1%temp1
part1=num1-part2
if(num1>part1):
    figword1(part1)
    figword1(part2)
print()

#This program will work from 21 to 99
