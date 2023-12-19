def convertUnits(path1,fname):
    f1 = open(path1+fname, "r")
    f2 = open(path1+"out_"+fname, "w")
    list2 = f1.readlines()
    len2 = len(list2)
    for i in range (0,len2,1):
        list1 = list2[i].replace("\n","").split(" ")
        lhs_value = float(list1[0])
        lhs_units = list1[1]
        separator = list1[2]
        rhs_value = float(list1[3])
        rhs_units = list1[4]
        info1 = str(1)+" "+lhs_units+separator+str(round(rhs_value/lhs_value, 2))+" "+rhs_units
        info2 = str(1)+" "+rhs_units+separator+str(round(lhs_value/rhs_value, 2))+" "+lhs_units
        print(info1)
        print(info2)
        print(" ")
        f2.write(info1)
        f2.write("\n")
        f2.write(info2)
        f2.write("\n")
        f2.write("\n")

    f2.close()
    
