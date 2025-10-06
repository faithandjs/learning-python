import math  # https://python.readthedocs.io/fr/stable/library/math.html

# ====================================================================================================
# BASIC PRINTING & STRINGS
# ====================================================================================================

# Triple quotes """ """ preserve whitespace/structure in a string
z = """
        Okay then, lol
        Stop playing with me
        """

# Newline character: \n
x = "Hey there, \nComo estas?"

# String length
# print(len('four'))

# String interpolation with f-strings
fname = 'faith'
lname = 'debs'
full = f'{fname} {lname}'
# print(full)

# String methods (original variable not altered, everything is an object in Python)
course = '   Python programming'
# print(course.upper())     # Uppercase
# print(course.lower())     # Lowercase
# print(course.strip())     # Remove whitespace
# print(course.title())     # Capitalize each word
# print(course.find('Pro')) # Find index of substring

# Membership checks
const = 'Pro' in course
constnt = 'Pro' not in course
# print(const, constnt)


# ====================================================================================================
# NUMBERS
# ====================================================================================================

# Types:
#   1      -> int
#   1.1    -> float
#   1 + 2j -> complex

# Operators: +, -, *, /, %, // (integer division), ** (power)
# print(10 / 6)
# print(10 % 3)
# print(10 // 6)
# print(10 ** 3)

x = 4
x += 4
# print(x)

# Built-in numeric functions
# print(round(2.7))   # Rounds
# print(abs(-2.7))    # Absolute value

# math module
# print(math.ceil(2.2))


# ====================================================================================================
# INPUT
# ====================================================================================================

# x = input("x: ")
# y = int(x) + 1
# print(f'x: {x}, y: {y}')


# ====================================================================================================
# BOOLEAN
# ====================================================================================================

# Falsy values: "", 0, None
# print(bool(0))

# Operators: >, >=, <=, <, ==, !=
# print(ord('b'), ord('B'))


# ====================================================================================================
# CONDITIONALS
# ====================================================================================================

temp = 15
if temp > 30:
    msg = 'Warm'
elif temp > 20:
    msg = 'Not Bad'
else:
    msg = 'Good'
# print(msg)

# Ternary operator
temp = 'Warm' if temp > 30 else 'Not Bad'
# print(temp)


# ====================================================================================================
# LOGICAL OPERATORS
# ====================================================================================================

# and, or, not
high_income = True
good_credit = True
student = True

if not (student and (high_income and good_credit)):
    status = 'Eligible'
else:
    status = 'Not Eligible'

# Chaining comparisons
age = 45
if 18 <= age > 65:
    msg = 'Window'
else:
    msg = 'Missed it'
# print(msg)


# ====================================================================================================
# LOOPS
# ====================================================================================================

# For loop with break
successful = False
for number in range(1, 10, 2):  # start, stop, step
    print("Attempt", number, number * '.')
    if number == 6:
        successful = True
    if successful:
        # print('Success')
        break
# else:
#     print('Failure')

# While loop
number = 100
# while number > 0:
#     number //= 2
#     print(number)

# While loop with user input
# command = ''
# while command != 'quit':
#     command = input('??')
#     print('ECHO', command)

# Counting even numbers
length = 0
for x in range(1, 10):
    if x % 2 == 0:
        length += 1
        # print(x)

# print(f'We have {length} even numbers')


# ====================================================================================================
# TYPES
# ====================================================================================================
# Primitive: str, int/float, bool
# Complex: range (e.g., range(5)). tuple, (2,3,4,5) - can't be altered. list [1,2,3,4] - .


# ====================================================================================================
# FUNCTIONS
# ====================================================================================================

def func_name(name):
    print(f'Hola {name}')


func_name('Lola')


def func_name(name):
    return f'Hola {name}'


print('Res:', func_name('Lola'))

# You can make a parameter optional by assigning it a value
# You can also call functions like: increment(4, by=4). Improves readability

#


def multiply(*numbers):
    print(numbers, type(numbers))


multiply(2, 3, 4, 5)
