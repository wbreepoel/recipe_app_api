"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class calcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test adding nr together"""
        sample_x = 5
        sample_y = 6

        res = calc.add(sample_x, sample_y)

        self.assertEqual(res,11)


    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10,2)

        self.assertEqual(res,8)