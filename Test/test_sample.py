import pytest_check as check
#hello

def test_one():
    check.equal("abcd","bbbb")

def test_two():
    check.greater(10,9)

def test_three():
    check.not_equal(2,4)
