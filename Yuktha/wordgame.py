def transform1(word):
    f1 = open("word2.txt", 'r')
    list1 = f1.read().split("\n")  # contain word elements
    list3 = []
    used_word=[]
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v','w', 'x', 'y', 'z']
    for i in range(0, 26, 1):
        if last_char == alpha[i]:
            list2=(list1[i])
            list3=list2.split(',')
            temp=list3[0]
            j=0
            for f in range(len(list3)):
                    input2 = temp

    return input2



print("enter english words:")
user_word=[]
for i in range (8):
       user =input()
       len2 = len(user)
       last_char = user[len2 - 1:len2]
       computer = transform1(user)
       print(user, computer)





