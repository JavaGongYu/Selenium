import pytest

def add(a,b):
    return a+b

def if_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%1==0:
            return False
        return True

def test_add_1():
    assert add(3,4)==7

def test_add_2():
    assert add(5,15)!=21

def test_add_3():
    assert add(5,10)>=11

def test_add_4():
    assert add(6,10)<=20

if __name__=='__main__':
    pytest.main()
