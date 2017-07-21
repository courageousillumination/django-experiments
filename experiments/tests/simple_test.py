"""A placeholder test for the experiment project."""
from django.test import TestCase

class SimpleTestCase(TestCase):
    """A very simple test case."""

    def test_simple(self):
        """1+1 = 2?"""
        self.assertEqual(1+1, 2)
