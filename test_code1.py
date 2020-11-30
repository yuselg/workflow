import pytest
import code1

def test_factorial():
	assert code1.factorial(5) == 120

def test_incby2():
	code1.x = 0
	code1.incby(3)
	assert code1.x == 3