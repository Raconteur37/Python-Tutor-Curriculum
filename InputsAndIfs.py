inp = input(f'Choose anything: ')
print(f'Your inp is: {inp}')
print()

realInt = int(input(f'Choose an integer: '))
print(f'This is our int: {realInt}')
print()

realString = str(input(f'Choose a string: '))
print(f'This is our string: {realString}')
print()

realFloat = float(input(f'Choose a float: '))
print(f'This is our float: {realFloat}')
print()

num = int(input(f'Choose a number: '))
print()

# If and else

if (num == 5):
    print(f'{num} is 5 :>')
else:
    print(f'{num} is not 5 :<')

if (num != 5):
    print(f'{num} is not 5 for sure')
    
if (num > 5):
    print(f'{num} is greater than 5!')
else:
    print(f'{num} is not greater than 5')
    
if (num < 5):
    print(f'{num} is less than 5')
else:
    print(f'{num} is not less than 5')
    
if (num == 4 or num == 3):
    print(f'{num} is 4 or 3 who knows')
    
if (num > 5 and num == 6):
    print(f'{num} is 6 and greater than 5!')    
        
    
print()
    
# Strings and elifs
    
string = str(input(f'Choose a string: '))

if (string == "cats"):
    print(f'Your string is cats!')
elif (string == "dogs"):
    print(f'Your string is dogs')
else:
    print(f'Your string isnt cats or dogs')

if (string.find("f") > -1): # Take what things return and compare
    print(f'f is in the string')
else:
    print(f'f is not in the string')
print()

    
    