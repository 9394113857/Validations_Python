import unittest
from validations import validate_email, validate_phone

class TestValidationFunctions(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(validate_email('test@example.com'))

    def test_invalid_email(self):
        self.assertFalse(validate_email('invalid_email'))

    def test_valid_phone(self):
        self.assertTrue(validate_phone('1234567890'))

    def test_invalid_phone(self):
        self.assertFalse(validate_phone('invalid_phone_number'))

if __name__ == '__main__':
    unittest.main()
