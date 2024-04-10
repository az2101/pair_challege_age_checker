# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.
_

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def age_checker(date_of_birth):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        date_of_birth: takes a string in form yyyy-mm-dd

    Returns: (state the return value and its type)
        a string either granting or denying access or throwing an error

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an dob making age above 16
Returns 'Access Granted!'
"""
age_checker("2005-04-09") => "Access Granted"

"""
Given an dob making age below 16
Returns 'Access denied. You are {age}, you must be over 16 to enter!'
"""
age_checker("2010-04-09") => "Access Denied. You are {age}, you must be over 16 to enter!"

"""
Given an invalid entry
It throws an error 'Invalid date format'
"""
age_checker('invalid') throws an error 'Invalid date format' 

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

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
    with pytest.raise(Exception) as e:
        age_checker('invalid') 
    error_message = str(e.value)
    criteria = 'Invalid date format' 
    assert criteria == error_message


```

Ensure all test function names are unique, otherwise pytest will ignore them!
