x = 0
while (x < 5):
    print(f'Woo!')
    x += 1
print()    


z = 10
while (z <= 10):
    print(z)
    if (z == 3):
        break 
    z -= 1
print()

run = True
myString = "a"
while (run):
    if (len(myString) == 5):
        print(myString)
        run = False
    myString += "a"
print()
    
# OR 

aString = "a"
while (len(aString) != 5):
    aString += "a"
print(aString)
print()