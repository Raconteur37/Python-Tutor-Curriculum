string1 = "Hello"
char = 'H'

print(f'{string1}')
print()

# Substrings

string = "Waiter"

num3 = string[2]
print(f'This is the string in position 2: {num3}')
print()

charsTo3 = string[:3]
print(f'These are strings in the positions 3 and below: {charsTo3}')
print()

charsPast3 = string[3:]
print(f'These are strings in position 3 and above: {charsPast3}')
print()

char5 = charsPast3[1]
print(f'This is the string in position 1: {char5}')
print()

lastChar = string[-1]
print(f'Last char in the string: {lastChar}')
print()

negChar = string[:-3]
print(f'Neg chars up to 4: {negChar}')
print()

slicedAddString = string[0:3] * 5
print(f'This is our sliced add string: {slicedAddString}')
print()

# Cases with strings

print(f'String lowercase: {string.lower()}')
print()

print(f'String uppercase: {string.upper()}')
print()

word = string + " and another waiter"
print(f'String as title: {word.title()}')
print()

print(f'String swapcase: {string.swapcase()}')
print()

# Managing strings

print(f'Letter W count: {word.count("W")}')
print()

print(f'Ends with er: {word.endswith("er")}')
print()

print(f'Ends with ed: {word.endswith("ed")}')
print()

print(f'ai is in position: {word.find("ai")}')
print()