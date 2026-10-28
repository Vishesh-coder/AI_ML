import pytest
from Python_tasks.task4 import sqr

def test_sqr_zero():
    assert sqr(0) == 0

def test_sqr_positive():
    assert sqr(5) == 25
    assert sqr(1) == 1
    assert sqr(10) == 100

def test_sqr_negative():
    assert sqr(-5) == 25
    assert sqr(-1) == 1
    assert sqr(-10) == 100

def test_sqr_float():
    assert sqr(2.5) == 6.25
    assert sqr(-2.5) == 6.25
    assert sqr(0.0) == 0.0
