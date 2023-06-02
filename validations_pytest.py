import pytest
from validations import validate_email, validate_phone

def test_valid_email():
    assert validate_email('test@example.com') == True

def test_invalid_email():
    assert validate_email('invalid_email') == False

def test_valid_phone():
    assert validate_phone('1234567890') == True

def test_invalid_phone():
    assert validate_phone('invalid_phone_number') == False
