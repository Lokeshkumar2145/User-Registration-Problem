import pytest
from main import validate_name, validate_email, validate_phone, validate_password, InvalidInput

def test_validate_name():
    assert validate_name("Lokesh", "Kumar") == "Lokesh Kumar is a valid name."
    with pytest.raises(InvalidInput):
        validate_name("lokesh", "kumar")

def test_validate_email():
    assert validate_email("abc.xyz@bl.com") == "abc.xyz@bl.com is a valid email."
    with pytest.raises(InvalidInput):
        validate_email("abc.xyz@bl")

def test_validate_phone():
    assert validate_phone("+91 9876543210") == "+91 9876543210 is a valid phone number."
    with pytest.raises(InvalidInput):
        validate_phone("9876543210")

def test_validate_password():
    assert validate_password("mypassword") == "Password is valid."
    with pytest.raises(InvalidInput):
        validate_password("abc@123")
