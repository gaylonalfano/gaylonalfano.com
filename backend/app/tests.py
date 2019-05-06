# backend/app/tests.py
# Import the Django TestCase. A class that has a bunch of helper functions
from django.test import TestCase

# Import function we're going to test
from app.calc import add, subtract

# Create the test class we want


class CalcTests(TestCase):

    # Create the test with two components. MUST start with "test"!
    # 1. Setup stage - Set your function up to be testing
    # 2. Assertion - Confirm that the output is equal to what it should be
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
