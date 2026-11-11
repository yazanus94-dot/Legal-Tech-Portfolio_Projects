import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from eosb import gratuity

def test_under_one_year():
    assert gratuity(10000, 0.9) == 0.0

def test_three_years():
    assert abs(gratuity(10000, 3) - (10000*12/365*21*3)) < 0.01

def test_cap_two_years():
    assert gratuity(10000, 40) == 240000.0
