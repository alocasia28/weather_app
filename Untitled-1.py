

listOfLists = [
                ["A","2","C"],
                ["D","4","F"],
                ["G","6","I"]
            ]
newList = []
for individualList in listOfLists:
    var1 = individualList[0]
    var2 = int(individualList[1])
    var3 = individualList[2]

    returnVar = [ var1,var2, var3 ]
    newList.append(returnVar)
print(newList)