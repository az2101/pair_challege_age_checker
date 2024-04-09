
import pytest
from lib.age_check import *

"""
Given an dob making age above 16
Returns 'Access Granted!'
"""
def test_age_checker_appropriate_age():
    criteria = "Access Granted"
    result = age_checker("2005-04-09")
    assert criteria == result

"""
Given an dob making age below 16
Returns 'Access denied. You are {age}, you must be over 16 to enter!'
"""
def test_age_checker_age_too_young():
    criteria = "Access denied. You are 14, you must be over 16 to enter!"
    result = age_checker("2010-04-09")
    assert criteria == result

"""
Given an invalid entry
It throws an error 'Invalid date format'
"""
def test_age_checker_invalid_age():
    with pytest.raises(ValueError):
        age_checker('invalid') 
    #error_message = str(e.value)
    #criteria = "Invalid date format"
    #assert criteria == error_message

""" Given a future date of birth
It throws an exception error 'Date is in the future'
"""
def test_age_checker_future_date():
    with pytest.raises(Exception) as e:
        age_checker('2030-04-09')
    error_message = str(e.value)
    assert error_message == 'Date is in the future'
