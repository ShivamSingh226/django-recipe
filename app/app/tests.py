"""
Sample Test Cases
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add_num(5, 6)
        self.assertEqual(res, 11)
