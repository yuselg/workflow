#!/usr/bin/env python3

def factorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

x: int = 0

def incby(i:int) -> None:
	assert i > 0
	global x
	x = x + i 

print("x:", x)
incby(4); incby(2)

print("x:", x)