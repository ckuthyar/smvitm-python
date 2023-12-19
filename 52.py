words=[["apple","art"],["blac","baby"],["cat","carrot"],["drum","day"],["eve","egg"],["fish","fan"],["goat","giraffe"],["horse","her"],["ink","idea"],["joke","jail"],["kite","kilogram"],["lovely","large"],["mango","man"],["nurse","nun"],["orange","owl"],["parrot","peacock"],["queen","quick"],["result","risk"],["smile","stay"],["train","test"],["umbrella","unit"],["very","velocity"],["water","well"],["xmas","xylophone"],["yes","yeast"],["zebra","zero"]]
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
used=[]

for i in range(0,10,1):
    input1=input("Enter a word: ")
    len1=len(input1)
    lastchar1=input1[len1-1:len1]
    used.append(input1)
    position1=alpha.index(lastchar1)
    wordlist=words[position1]
    input2=wordlist[0]
    used.append(input2)
    print(used)
