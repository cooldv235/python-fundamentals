# A Variable is a container for a value, which can be of varous types

'''
    This is a multi
    line comment
    or docstring (in python) (used to define a function's purpose)
    can be single or double quotes
'''

"""
    VARIABLE RULES:
    - Variable names are case sensitive (name and NAME are two different variables)
    - Must start with a letter or an underscore
    - Can have numbers but cannot have special symbols and cannot start with any of these two
"""

# x = 1                   # int
# y = 2.5                 # float
# name = 'Dushyant'       # str
# is_cool = True          # bool

# Multiple assignment in one single line
x,y,name,is_cool = (1,2.3,'Dushyant',True)

print(x,y,name,is_cool)

# Print type of a variable
print(type(x))

# Casting
x = str(x)
y = int(y)              # Will lose its decimal value
z = float(y)            # 2.0
print(type(x))
print(type(y),y)
print(z)

