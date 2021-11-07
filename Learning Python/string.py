name = 'Maithili'
age = 24

# concatenate

print('Hello, my name is ' + name + ' and I am ' + str(age))

# string formatting

# 1. Arguments by position
# here {x} & {y} are just placeholders and we don't need to convert integer to string format.
print('My name is {x} and I am {y}' .format(x = name, y = age))

# 2. F-string (can be used in python 3.6+ )
print(f'My name is {name} and I am {age}')

# string Methods

s = 'hello world'

# 1. Capitalize string - it is a function so need to put parenthisis
print(s.capitalize())

# 2. Make all upper 
print(s.upper())

# 3. Make all lower
print(s.lower())

# 4. Swap case
print(s.swapcase())

# 5. Get length
print(len(s))

# 6. Replace
print(s.replace('world', 'everyone'))

# 7. Count
sub = 'h'
print(s.count(sub))

# 8. Starts with
print(s.startswith('hello'))

# 9. Ends with
print(s.endswith('d'))

# 10. Split into the list
print(s.split())

# 11. Find position
print(s.find('r'))

# 12. Is all alphanumeric
print(s.isalnum())

# 13. Is all alphabetic
print(s.isalpha())

# 14. Is all numeric
print(s.isnumeric())



