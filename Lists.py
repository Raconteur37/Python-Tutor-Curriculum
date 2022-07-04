stringList = ["cat","dog","fish","bird"]
firstWord = stringList[0]
print(f'This is the list: {stringList}')
print(f'First word in the list: {firstWord}')
print()

intList = [1,2,3,4]
firstNum = intList[0]
print(f'First number on list: {firstNum}')
print()

addInts = intList[0] + intList[3]
print(f'Adding ints: {addInts}')
print()

crazyStr = stringList[2][:3]
print(f'Crazy str: {crazyStr}')
print()

longList = [1,4,8,3,5,1,9,10]
print(f'Length of the list {len(longList)}')
print()

mixedList = [1,"dogs",True,2.7,"cats"]
print(mixedList)
print()

aList = [1,2,3,4,5]
print(aList)
aList.append(6)
print(aList)
print()

aList[0] = -1
print(aList)
print()

aList.remove(3)
print(aList)
print()

aList.pop(0)
print(aList)
print()

# OR

del aList[0]
print(aList)
print()

aList.clear()
print(aList)
print()

aList = [1,2,3,4,5]
for x in aList:
    print(x)
    
print()
# OR

x = 0
while (x < len(aList)):
    print(aList[x])
    x+=1
print()