def addNum():
    print (1+5)

def superAddNum(x,y):
    print (x + y)
    
def returnNum(x):
    return (x)

def doMath(x,y):
    x = x + 5
    y = y + 10
    total = x + y
    return (total)

total = doMath(4,5)
print(total)

def findA(word:str):
    return (word.find("a"))

print(f'A is at {findA("dogsa")}')

def getFirst(aList:list):
    return (aList[0])

def getFirstNon(aList):
    return (aList[0])

oneList = ["f","x","z","u","p"]

print(f'{getFirst(oneList)}')