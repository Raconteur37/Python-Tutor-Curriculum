string1 = "Hello"

print(f'{string1}')
print()

# Substrings

string = "waiter"

num3 = string[2]
print(f'This is the string in position 2: {num3}')
print()

numsTo3 = string[:3]
print(f'These are strings in the positions 3 and below: {numsTo3}')
print()

numsPast3 = string[3:]
print(f'These are strings in position 3 and above: {numsPast3}')
print()

num5 = numsPast3[1]
print(f'This is the string in position 1: {num5}')
print()

lastNum = string[-1]
print(f'Last char in the string: {lastNum}')
print()