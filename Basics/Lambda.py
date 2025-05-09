#!Python Lambda

#Syntax : lambda argument : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5,6))

x = lambda a, b, c : a + b + c
print(x(2, 3, 4))

#! Why we lambda function : When anonymous function is required for a short period of times

#* Say I have the function definition that makes one argument, and that argument will be mutiplied with an unknown number

def function(n):
    return lambda a : a * n

double = function(2)

print(double(11))


def function(n):
    return lambda a : a * n

double = function(2)
tripler = function(3)

print(double(15))
print(tripler(52))