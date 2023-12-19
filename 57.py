response2={"data": [
        {
            "id": "g6-nanode-1",
            "label": "Nanode 1GB",
            "price": {
                "hourly": 0.0075,
                "monthly": 5.0
            }
        }
    ]
}
response3=list(response2.values())
response4=response3[0][0]
list1=list(response4.keys())
list2=list(response4.values())

#print(list1)
#print(list2)

f2=open("faq.txt","w")


line1="What is the price of" + list2[0] + " in US dollars"
line2= str(list2[2])
print(line1)
f2.write(line1)
f2.write("\n")
print(line2)
f2.write(line2)
f2.write("\n")
print()
f2.close()

print("What is the RAM available for",list2[0])
print(list2[1].replace("Nanode",""))
print()
