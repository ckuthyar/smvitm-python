import datetime as dt
import mod_rule1
import mod_rule2
import mod_rule4
import mod_rule

s1="enter a word which is not used before by either player or computer"
s2="player is disqualified due to rule 3"
s3="player has entered the word"
s4='enter a word with in 30 seconds : '
s5='player is disqualified due to rule 4'
s6="No more English words in Computer's memory......\nCOMPUTER HAS LOST THE GAME"
s7='player is disqualified due to rule 2'
s8='player is disqualified due to rule 1'

output = mod_rule1.transform1('word2.txt')
complist=output
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
used=[]
input1=[]
input2=[]
lastchar=''
computer1=0
total1,player=0,0
total2,computer=0,0


input2='hello'
print("**********WELCOME TO WORD GAME **********")
print("BEFORE YOU BEGIN THE GAME REMEMBER 4 RULES:")
print("1) Word should be an English word\n2) Starting letter should be same as ending letter of Player/Computer")
print("3) Word should not be repeated\n4) Word should be input before 30 seconds")
print("\n")
print("computer has started the game")
print(input2)
print(s4)

while True:

    #FOR PLAYER
    timeout = 30
    result = mod_rule4.rule4(timeout)
    time1 = result[0]
    input1 = result[1]
    if (time1 > timeout):
        print(s5)
        break
    alphabet=mod_rule.rule(input1)
    if not alphabet:
        print(s8)
        break

    lastchar = input2[-1]
    isdisqualified = mod_rule2.rule2(lastchar, input1)
    if isdisqualified:
        print(s7)
        break
    if input1 in used:
        print(s1)
        input1 = input()
        if input1 in used:
            print(s2)
            break
        else:
            used.append(input1)
    else:
        used.append(input1)

     # FOR COMPUTER

    lastchar = input1[-1]
    position1 = alpha.index(lastchar)
    templist1=complist[position1]
    input2 =templist1[0]
    firstchar = input2[0:1]
    index1 = alpha.index(firstchar)
    currentlist = complist[index1]
    if input2 in used:
        if input2 in currentlist:
            currentlist.remove(input2)
            if currentlist == [] :
                print(s6)
                computer1=1
                break
            input2 = complist[position1][0]
            used.append(input2)
    else:
        used.append(input2)

    print(input1,"-", input2)
    player = len(input1)
    total1 += player
    computer = len(input2)
    total2 += computer

print("SCORE OF PLAYERS")
print("PLAYER : ",total1)
print("COMPUTER : ",total2)
if computer1 == 1:
    print("\n PLAYER IS THE WINNER")
else:
    if total1 > total2:
        print("\n PLAYER IS THE WINNER")
    else:
        print("\n COMPUTER IS THE WINNER")
