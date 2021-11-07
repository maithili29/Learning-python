#  Variable can be considered as the name given to the storage space.
# --  cannot use keywords


# x = 2             # int
# y = 2.5           # float
# name = 'John'     # str
# is_cool = True    # bool if we write true like this then it will called as variable

# Multiple Assignment
x, y, name, is_cool = (2, 2.5, 'John', True)
print(x, y, name, is_cool)

# Basic math
a = x + y
print(a)

# type() returns the datatype of that variable
print(type(x))
print(type(y))

# casting : Used to change the datatypes of a variable

x = str(x)
y = int(y)
z = float(y)

# here the value of y will be whole number.
print(type(y), y)

# here the value of z will be 2.0 because when we converted it to int it was 2 and not 2.5
print(type(z), z)
