import math

word = "Hello!" # String inside of a variable

integer = 2 # Integer inside of a variable

flt = 2.5 # Float inside of a variable

# The f in the print statement means formatting a literal variable into a string
print()
print(f'This is our word: {word}') 
print(f'This is our integer: {integer}')
print(f'This is our float: {flt}')

# Adding integers and floats

num1 = 5

num2 = 10

total = num1 + num2 # Total is an integer
print()
print(f'This is our total {total}')

flt1 = 2.5 

total = num1 + flt1 # Total is now a float

print()
print(f'This is our float total: {total}')

print("This is out float total: " + str(total))
print()

# Main operator types, +, -, *, /, and %

addNum = 10 + 5 # Addition

subNum = 10 - 5 # Subtraction

multNum = 5 * 5 # Multiplication

divNum = 10 / 5 # Division

modNum = 10 % 5 # Modulus

print(f'This is our add total: {addNum}')
print(f'This is our subtract total: {subNum}')
print(f'This is our multiplication total: {multNum}')
print(f'This is our division total: {divNum}')
print(f'This is our modulus total: {modNum}')
print()

# Advanced math types

floorNum = math.floor(4.7)
print(f'This is our floorNum: {floorNum}')

ceilNum = math.ceil(4.2)
print(f'This is our ceilNum: {ceilNum}')
print()

roundNum1 = 4.6 # If this was 4.5 it would round down!
roundNum2 = 4.2

# Notice how it starts as a float then rounds to an int

roundTotal1 = round(roundNum1)
roundTotal2 = round(roundNum2)

print(f'{roundNum1} rounded is {roundTotal1}')
print(f'{roundNum2} rounded is {roundTotal2}')
print()
