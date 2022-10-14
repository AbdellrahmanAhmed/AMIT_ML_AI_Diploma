from code import *

a = int(input('number 1: '))
b = int(input('number 2: '))
cal()
z = input('Make your choice:  ')

if z[0] == '1':
    add(a, b)
elif z[0] == '2':
    sub(a, b)
elif z[0] == '3':
    mal(a, b)
elif z[0] == '4':
    div(a, b)