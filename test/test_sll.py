from sll import *

def test_sll_create():
    test1 = linkst()
    assert test1.empty() 

def test_sll_add():
    test1 = linkst()
    test1.append("yan")
    test1.append("ji")
    assert "yan" in test1

def test_sll_insert():
    test1 = linkst()
    test1.append("yan")
    test1.append("ji")
    test1.insert("cheng")
    assert "cheng" in test1

def test_sll_print():
    test1 = linkst()
    test1.append("yan")
    test1.append("ji")
    print(test1)
    assert "yan->ji" == str(test1)
