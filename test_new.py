import pytest

def sum(a,b):
    return a+b

def test_file1():
    assert sum(5,6) == 11,"test passed"
    # assert sum(15,6) == 11,"test failed"
    assert sum(5,1) == 6,"test passed"


# def test_file1_method1():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"
# 	assert x == y,"test failed"
# def test_file1_method2():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed" 