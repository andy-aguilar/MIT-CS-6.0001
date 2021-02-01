import numpy

x = input("Enter number x:")
while not str.isnumeric(x):
    x = input("That ain't no number! Enter number x:")
x = int(x)

y = input("Enter number y:")
while not str.isnumeric(y):
    y = input("That ain't no number! Enter number y:")
y = int(y)

print(f'x**y = {x**y}')
print(f'log(x) = {numpy.log2(x)}')