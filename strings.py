# Strings in python are surrounded by either single or double quotes 

firstName = 'Dushyant'
lastName = "Vishwakarma"
age = 26

# Concatenate
# print('Hello, my name is ' + firstName + ' and I am ' + age)    # TypeError: must be str, not int
print('Hello, my name is ' + firstName + ' and I am ' + str(age))    # TypeError: must be str, not int

# Arguments by position
print('My name is {name} and I am {age}'. format(name=firstName,age=age))

# F-Strings 3.6+ only
print(f'Hello, my name is {firstName} and I am {age}')

# String methods
s = 'hello world'

# Capitalize
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world','everyone'))

# Count
sub = 'h'
print(s.count(sub))     # counts the no. of h inside the string

# Starts with
print(s.startswith('hello'))    # returns true if str starts with hello else false

# Ends with
print(s.endswith('d'))  # returns true if str ends with d else false

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalpha())          # returns true if all letters are alphanumeric

# Is all numeric
print(s.isnumeric())